#!/usr/bin/env python3
"""
Convert all documentation files to Australian English orthographic conventions
"""
import os
import re
from pathlib import Path

# Australian English spelling conversions
CONVERSIONS = {
    # -ize → -ise
    r'\b(organ|optim|recogn|categor|prior|visual|summar|specialis|realis|maxim|minim|author|character|custom|general|final|normal|synthes|anal)iz(e|es|ed|ing|ation|ations)\b': r'\1is\2',

    # -yze → -yse
    r'\b(anal|paral)yz(e|es|ed|ing)\b': r'\1ys\2',

    # -or → -our (but not in -ior, -sor endings)
    r'\b(behavi|col|fav|flav|hono|lab|neighb|rum|sav|vap|harb|arm)or\b': r'\1our',
    r'\b(behavi|col|fav|flav|hono|lab|neighb|rum|sav|vap|harb|arm)ors\b': r'\1ours',

    # -ense → -ence (for licence/licence as noun, defence/defence)
    r'\bdefense\b': 'defence',
    r'\bDefense\b': 'Defence',
    r'\bdefenses\b': 'defences',
    r'\bDefenses\b': 'Defences',
    r'\boffense\b': 'offence',
    r'\bOffense\b': 'Offence',
    r'\boffenses\b': 'offences',
    r'\blicense\b': 'licence',  # as noun
    r'\bLicense\b': 'Licence',

    # -er → -re
    r'\b(cent|met|theat|spectr|fib|calibr|meag|salit)er\b': r'\1re',
    r'\b(cent|met|theat|spectr|fib|calibr|meag|salit)ers\b': r'\1res',

    # -og → -ogue
    r'\b(catal|dial|anal|prol|epil|monol)og\b': r'\1ogue',
    r'\b(catal|dial|anal|prol|epil|monol)ogs\b': r'\1ogues',

    # -l → -ll (travelling → travelling, etc.)
    r'\b(trav|marv|wooll|quarr|app|jewel)el(ed|ing|er|ers)\b': r'\1ell\2',
    r'\b(trav|marv|wooll|quarr|app|jewel)el(s)\b': r'\1el\2',  # but not double for plural

    # -eled → -elled
    r'\b(lab|mod|trav|marv|fuel|duel|jewel|quarrel|apparel|barrel|carol|channel|counsel|dial|duel|fuel|funnel|jewel|label|libel|marvel|model|panel|pencil|quarrel|rival|signal|spiral|travel|tunnel)el(ed|ing|er|ers)\b': r'\1ell\2',

    # Specific common words
    r'\banalyze\b': 'analyse',
    r'\bAnalyze\b': 'Analyse',
    r'\banalyzes\b': 'analyses',
    r'\bAnalyzes\b': 'Analyses',
    r'\banalyzing\b': 'analysing',
    r'\bAnalyzing\b': 'Analysing',
    r'\banalyzed\b': 'analysed',
    r'\bAnalyzed\b': 'Analysed',

    r'\borganize\b': 'organise',
    r'\bOrganize\b': 'Organise',
    r'\borganizes\b': 'organises',
    r'\borganizing\b': 'organising',
    r'\borganized\b': 'organised',
    r'\borganization\b': 'organisation',
    r'\bOrganization\b': 'Organisation',
    r'\borganizations\b': 'organisations',
    r'\bOrganizations\b': 'Organisations',

    r'\brecognize\b': 'recognise',
    r'\bRecognize\b': 'Recognise',
    r'\brecognizes\b': 'recognises',
    r'\brecognizing\b': 'recognising',
    r'\brecognized\b': 'recognised',
    r'\brecognition\b': 'recognition',  # stays same

    r'\boptimize\b': 'optimise',
    r'\bOptimize\b': 'Optimise',
    r'\boptimizes\b': 'optimises',
    r'\boptimizing\b': 'optimising',
    r'\boptimized\b': 'optimised',
    r'\boptimization\b': 'optimisation',
    r'\bOptimization\b': 'Optimisation',
    r'\boptimizations\b': 'optimisations',

    r'\bvisualize\b': 'visualise',
    r'\bVisualize\b': 'Visualise',
    r'\bvisualizes\b': 'visualises',
    r'\bvisualizing\b': 'visualising',
    r'\bvisualized\b': 'visualised',
    r'\bvisualization\b': 'visualisation',
    r'\bVisualization\b': 'Visualisation',
    r'\bvisualizations\b': 'visualisations',
    r'\bVisualizations\b': 'Visualisations',

    r'\bcategorize\b': 'categorise',
    r'\bCategorize\b': 'Categorise',
    r'\bcategorizes\b': 'categorises',
    r'\bcategorizing\b': 'categorising',
    r'\bcategorized\b': 'categorised',
    r'\bcategorization\b': 'categorisation',

    r'\bspecialize\b': 'specialise',
    r'\bSpecialize\b': 'Specialise',
    r'\bspecialized\b': 'specialised',
    r'\bspecializes\b': 'specialises',
    r'\bspecializing\b': 'specialising',
    r'\bspecialization\b': 'specialisation',

    r'\bsummarize\b': 'summarise',
    r'\bSummarize\b': 'Summarise',
    r'\bsummarizes\b': 'summarises',
    r'\bsummarizing\b': 'summarising',
    r'\bsummarized\b': 'summarised',

    r'\bauthorize\b': 'authorise',
    r'\bAuthorize\b': 'Authorise',
    r'\bauthorizes\b': 'authorises',
    r'\bauthorizing\b': 'authorising',
    r'\bauthorized\b': 'authorised',
    r'\bauthorization\b': 'authorisation',
    r'\bAuthorization\b': 'Authorisation',

    r'\brealize\b': 'realise',
    r'\bRealize\b': 'Realise',
    r'\brealizes\b': 'realises',
    r'\brealizing\b': 'realising',
    r'\brealized\b': 'realised',
    r'\brealization\b': 'realisation',

    r'\bcharacterize\b': 'characterise',
    r'\bCharacterize\b': 'Characterise',
    r'\bcharacterizes\b': 'characterises',
    r'\bcharacterizing\b': 'characterising',
    r'\bcharacterized\b': 'characterised',

    r'\bcustomize\b': 'customise',
    r'\bCustomize\b': 'Customise',
    r'\bcustomizes\b': 'customises',
    r'\bcustomizing\b': 'customising',
    r'\bcustomized\b': 'customised',
    r'\bcustomization\b': 'customisation',

    r'\bminimize\b': 'minimise',
    r'\bMinimize\b': 'Minimise',
    r'\bminimizes\b': 'minimises',
    r'\bminimizing\b': 'minimising',
    r'\bminimized\b': 'minimised',

    r'\bmaximize\b': 'maximise',
    r'\bMaximize\b': 'Maximise',
    r'\bmaximizes\b': 'maximises',
    r'\bmaximizing\b': 'maximising',
    r'\bmaximized\b': 'maximised',

    r'\bfinalize\b': 'finalise',
    r'\bFinalize\b': 'Finalise',
    r'\bfinalizes\b': 'finalises',
    r'\bfinalizing\b': 'finalising',
    r'\bfinalized\b': 'finalised',

    r'\bnormalize\b': 'normalise',
    r'\bNormalize\b': 'Normalise',
    r'\bnormalizes\b': 'normalises',
    r'\bnormalizing\b': 'normalising',
    r'\bnormalized\b': 'normalised',
    r'\bnormalization\b': 'normalisation',

    r'\bcolor\b': 'colour',
    r'\bColor\b': 'Colour',
    r'\bcolors\b': 'colours',
    r'\bColors\b': 'Colours',
    r'\bcolored\b': 'coloured',
    r'\bcoloring\b': 'colouring',
    r'\bcolorful\b': 'colourful',

    r'\bbehavior\b': 'behaviour',
    r'\bBehavior\b': 'Behaviour',
    r'\bbehaviors\b': 'behaviours',
    r'\bBehaviors\b': 'Behaviours',
    r'\bbehavioral\b': 'behavioural',
    r'\bBehavioral\b': 'Behavioural',

    r'\bfavor\b': 'favour',
    r'\bFavor\b': 'Favour',
    r'\bfavors\b': 'favours',
    r'\bfavored\b': 'favoured',
    r'\bfavorite\b': 'favourite',
    r'\bFavorite\b': 'Favourite',
    r'\bfavorites\b': 'favourites',

    r'\bhonor\b': 'honour',
    r'\bHonor\b': 'Honour',
    r'\bhonors\b': 'honours',
    r'\bhonored\b': 'honoured',

    r'\blabor\b': 'labour',
    r'\bLabor\b': 'Labour',
    r'\blabors\b': 'labours',

    r'\bneighbor\b': 'neighbour',
    r'\bNeighbor\b': 'Neighbour',
    r'\bneighbors\b': 'neighbours',
    r'\bneighborhood\b': 'neighbourhood',

    r'\bvapor\b': 'vapour',
    r'\bVapor\b': 'Vapour',

    r'\bharbor\b': 'harbour',
    r'\bHarbor\b': 'Harbour',
    r'\bharbors\b': 'harbours',

    r'\bcenter\b': 'centre',
    r'\bCenter\b': 'Centre',
    r'\bcenters\b': 'centres',
    r'\bcentered\b': 'centred',
    r'\bcentering\b': 'centring',

    r'\bmeter\b': 'metre',
    r'\bMeter\b': 'Metre',
    r'\bmeters\b': 'metres',

    r'\bliter\b': 'litre',
    r'\bLiter\b': 'Litre',
    r'\bliters\b': 'litres',

    r'\bfiber\b': 'fibre',
    r'\bFiber\b': 'Fibre',
    r'\bfibers\b': 'fibres',

    r'\bcatalog\b': 'catalogue',
    r'\bCatalog\b': 'Catalogue',
    r'\bcatalogs\b': 'catalogues',

    r'\bdialog\b': 'dialogue',
    r'\bDialog\b': 'Dialogue',
    r'\bdialogs\b': 'dialogues',

    r'\blabeled\b': 'labelled',
    r'\bLabeled\b': 'Labelled',
    r'\blabeling\b': 'labelling',

    r'\btraveled\b': 'travelled',
    r'\bTraveled\b': 'Travelled',
    r'\btraveling\b': 'travelling',
    r'\btraveler\b': 'traveller',
    r'\bTraveler\b': 'Traveller',
    r'\btravelers\b': 'travellers',

    r'\bmodeled\b': 'modelled',
    r'\bModeled\b': 'Modelled',
    r'\bmodeling\b': 'modelling',

    r'\bleveled\b': 'levelled',
    r'\bLeveled\b': 'Levelled',
    r'\bleveling\b': 'levelling',

    r'\bfueled\b': 'fuelled',
    r'\bFueled\b': 'Fuelled',
    r'\bfueling\b': 'fuelling',
}

# Exceptions - words that should NOT be converted
EXCEPTIONS = [
    'quantization',  # Technical ML term - keep American
    'tokenization',  # Technical ML term - keep American
    'vectorization',  # Technical ML term - keep American
    'tokenizer',
    'optimizer',  # PyTorch class name
    'Organisation',  # In organisation names like "World Health Organisation"
    'authorized_keys',  # SSH/Linux technical term
]

def convert_text(text: str) -> str:
    """Convert American English to Australian English"""
    converted = text

    for american, australian in CONVERSIONS.items():
        converted = re.sub(american, australian, converted)

    return converted

def should_process_file(filepath: Path) -> bool:
    """Determine if file should be processed"""
    # Skip certain directories
    skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
    if any(skip in filepath.parts for skip in skip_dirs):
        return False

    # Process markdown and Python files
    if filepath.suffix in {'.md', '.py', '.ipynb', '.txt'}:
        return True

    # Skip if in models/ directory checkpoints
    if 'checkpoint-' in str(filepath):
        return False

    return False

def convert_file(filepath: Path) -> bool:
    """Convert a single file to Australian English"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        converted = convert_text(content)

        if converted != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(converted)
            return True
        return False
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    """Convert all documentation to Australian English"""
    root = Path('/home/tinyai/ai_security_education')

    print("🇦🇺 Converting documentation to Australian English...")
    print("=" * 80)

    files_converted = 0
    files_processed = 0

    # Find all documentation files
    for filepath in root.rglob('*'):
        if filepath.is_file() and should_process_file(filepath):
            files_processed += 1
            relative_path = filepath.relative_to(root)

            if convert_file(filepath):
                files_converted += 1
                print(f"✅ Converted: {relative_path}")
            else:
                print(f"⏭️  No changes: {relative_path}")

    print("=" * 80)
    print(f"\n📊 Summary:")
    print(f"   Files processed: {files_processed}")
    print(f"   Files converted: {files_converted}")
    print(f"   Files unchanged: {files_processed - files_converted}")
    print("\n✅ Conversion complete!")

if __name__ == "__main__":
    main()
