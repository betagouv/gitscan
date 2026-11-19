## Changelog : anssi-recommandations-cyber (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans l'optimisation de son moteur d'intelligence artificielle. Les capacités de traitement ont été considérablement améliorées grâce à l'introduction de modes de calcul en parallèle et par lots, permettant des réponses plus rapides et plus précises. La fiabilité des recommandations est renforcée par une meilleure gestion des preuves extraites des guides de l'ANSSI.

### Évolutions fonctionnelles
- **Amélioration de la précision des réponses** : Optimisation de la sélection et de la fusion des preuves pour garantir que les recommandations s'appuient sur les segments de documents les plus pertinents.
- **Meilleure traçabilité des sources** : Conservation systématique des unités sources (pages et métadonnées) pour les paragraphes enrichis, permettant de mieux situer l'origine de l'information.

### Évolutions techniques
- **Optimisation du moteur de reclassement LLM** :
    - Introduction d'un mode de reclassement en parallèle pour augmenter la vitesse de traitement.
    - Ajout d'un mode de reclassement par lots pour une gestion plus structurée des données.
    - Mise en place d'un coordinateur pour gérer la capacité de traitement et limiter les appels simultanés.
- **Refactoring et architecture** :
    - Restructuration du code pour isoler les modèles de données (notamment pour les guides MSC) et améliorer la modularité.
    - Utilisation de "factories" pour l'instanciation des composants et meilleure séparation des domaines (domaine `question`).
    - Amélioration de la gestion des erreurs et des contrats de données (schémas JSON) pour les échanges avec l'IA.
- **Déploiement et Sécurité** :
    - Support du déploiement sur l'environnement de production "OFF".
    - Désactivation de l'outil de suivi Matomo pour renforcer la confidentialité.

### Autres changements
- **Documentation** : Mise à jour du modèle C4 et du fichier README.md.
- **Qualité du code** : Application de règles de formatage (Prettier) et nettoyage général du code.
