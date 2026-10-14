## Changelog : anssi-recommandations-cyber (30 derniers jours, au 05/10/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision et de la pertinence des réponses fournies par l'intelligence artificielle. L'accent a été mis sur l'optimisation de la manière dont le système extrait et enrichit les informations issues des guides de l'ANSSI, garantissant ainsi des recommandations plus fiables et mieux contextualisées pour l'utilisateur.

### Évolutions fonctionnelles
- **Amélioration de la précision des sources** : Les réponses priorisent désormais les preuves et références directement issues du guide correspondant au sujet traité.
- **Optimisation de l'enrichissement** : Le processus d'enrichissement des paragraphes a été amélioré pour fournir des informations plus complètes après une recherche.

### Évolutions techniques
- **Optimisation de la gestion du contexte** : 
    - Mise en place d'une nouvelle stratégie d'enrichissement basée sur l'analyse des pages adjacentes.
    - Garantie d'un contexte documentaire unique par paragraphe enrichi pour éviter les mélanges d'informations.
- **Amélioration du découpage des données (chunking)** : Optimisation de la segmentation pour éviter que des segments de texte ne soient partagés entre plusieurs paragraphes enrichis.
- **Exposition des données** : Amélioration de l'accès aux segments (chunks) paginés provenant du modèle Albert.
