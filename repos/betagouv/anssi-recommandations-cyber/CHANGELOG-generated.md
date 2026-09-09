## Changelog : anssi-recommandations-cyber (30 derniers jours, au 04/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision et de la fiabilité des réponses fournies par l'intelligence artificielle Albert. Le projet a également bénéficié d'une campagne importante de mises à jour de sécurité pour corriger des vulnérabilités dans les dépendances.

### Évolutions fonctionnelles
- **Amélioration de la qualité des réponses** : Stabilisation du formatage des listes Markdown dans les réponses de l'IA.
- **Précision des citations** : Renforcement de la fidélité des références aux documents sources en utilisant des repères système (document, section, recommandation) plutôt que de dépendre uniquement des balises OCR.

### Évolutions techniques
- **Optimisation du moteur d'IA (LLM)** :
    - Enrichissement du contexte envoyé au modèle avec des métadonnées précises (type de bloc, code de recommandation, chemin des sections).
    - Fiabilisation du processus de reclassement par le LLM en utilisant ces métadonnées comme signaux prioritaires.
    - Mise en place d'une propagation robuste des métadonnées de segmentation (chunks) depuis l'API jusqu'au modèle de données, assurant la compatibilité entre les anciens et les nouveaux index.
- **Sécurité** :
    - Application de correctifs de sécurité sur plusieurs dépendances critiques (`nanoid`, `pip`, `idna`, `cryptography`, `dompurify`, `pdfjs-dist`).

### Autres changements
- **Documentation** : Mise à jour du README et du descriptif du parcours d'interaction avec l'IA Albert.
