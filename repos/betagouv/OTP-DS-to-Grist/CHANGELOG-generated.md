## Changelog : OTP-DS-to-Grist (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'outil de synchronisation entre Démarches Simplifiées et Grist au cours des 30 derniers jours. Les modifications se concentrent principalement sur l'amélioration de l'interface utilisateur, notamment le formulaire de configuration, avec des ajustements pour une meilleure expérience et une plus grande clarté. Des corrections de bugs et des optimisations ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de textes d'aide et de liens pour faciliter la saisie des tokens d'API. (#177)
- Amélioration de l'interface du formulaire de configuration :
    - Messages de connexion déplacés pour une meilleure lisibilité.
    - Suppression d'un bandeau de statut redondant.
    - Fermeture automatique des volets "Données Nommées" et "Grist" lors de la synchronisation.
    - Fermeture du volet "Paramètres" lors de la synchronisation.
    - Placement du message de synchronisation en haut du formulaire.
    - Suppression de la notification de succès de sauvegarde.
    - Ajout de placeholders masqués pour les tokens déjà enregistrés.
    - Amélioration de l'espacement et de l'alignement des éléments.
- Ajout d'un bouton pour copier les logs de synchronisation. (#171)
- Ajout d'un bandeau d'information indiquant que l'outil est en version BETA. (#179)
- Suppression du bouton de menu mobile et refonte du menu principal. (#183)
- Correction d'un bug empêchant la synchronisation automatique sans clé Grist. (#202)

### Évolutions techniques
- Optimisation du code. (#164)
- Mise à jour des dépendances :
    - `sqlalchemy` vers la version 2.0.46
    - `poethepoet` vers la version 0.40.0
    - `python-socketio` vers la version 5.16.0
    - `apscheduler` vers la version 3.11.2
    - `commitizen` vers la version 4.12.1
    - `baseline-browser-mapping` vers la version 2.9.18

### Autres changements
- Nettoyage du CHANGELOG.md (#188)
- Amélioration de la configuration du projet avec VS Code. (#203)
- Publication de la version 0.6.0.
