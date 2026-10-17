## Changelog : anssi-recommandations-cyber (30 derniers jours, au 05/10/2026)

### Résumé
Les récentes évolutions visent à améliorer la précision et la fiabilité des réponses fournies par l'intelligence artificielle. L'outil est désormais plus performant pour extraire et présenter des preuves pertinentes issues des guides de l'ANSSI, tout en évitant les confusions d'informations lors de la génération de texte.

### Évolutions fonctionnelles
- Amélioration de la pertinence des réponses en priorisant les preuves issues du guide spécifiquement lié au sujet traité.

### Évolutions techniques
- Optimisation de la gestion du contexte documentaire pour l'enrichissement des paragraphes :
    - Isolation du contexte par paragraphe pour garantir une meilleure cohérence.
    - Suppression du partage de segments de texte (*chunks*) entre les différents paragraphes enrichis afin d'éviter les mélanges d'informations.
