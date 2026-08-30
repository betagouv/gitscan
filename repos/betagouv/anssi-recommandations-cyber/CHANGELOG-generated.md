## Changelog : anssi-recommandations-cyber (30 derniers jours, au 18 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la précision et de la fiabilité des réponses fournies par l'IA Albert. En enrichissant les données transmises au modèle avec des informations structurelles issues des guides de l'ANSSI (sections, codes de recommandation), l'outil garantit des citations plus fidèles et un meilleur classement des informations.

### Évolutions fonctionnelles
- **Amélioration de la précision des réponses** : l'IA dispose désormais d'un contexte enrichi, permettant de fournir des citations plus exactes et mieux contextualisées en s'appuyant sur la structure réelle des documents.

### Évolutions techniques
- **Optimisation du contexte LLM** : intégration de repères système (document, section, recommandation) pour fiabiliser la fidélité des citations sans dépendre uniquement des balises OCR.
- **Enrichissement et propagation des métadonnées** : déploiement de nouvelles métadonnées de structure (type de bloc, code de recommandation, chemin des sections) de l'API vers les modèles de données, avec une gestion de la compatibilité pour les données déjà indexées.
- **Fiabilisation du reclassement par l'IA** : utilisation des métadonnées structurées comme signaux prioritaires pour le processus de reclassement, l'analyse textuelle ne servant plus que de solution de repli.

### Autres changements
- **Documentation** : mise à jour du README et de la description du parcours d'interaction avec l'IA Albert.
