## Changelog : renovate-config (30 derniers jours, au 06/11/2026)

### Résumé
Lancement du projet avec la mise en place d'une configuration partagée pour automatiser la mise à jour des dépendances. Ce nouvel outil permet d'harmoniser les processus de maintenance sur l'ensemble des projets et inclut des contrôles automatiques pour garantir la fiabilité des configurations.

### Évolutions fonctionnelles
- Création et mise à disposition du preset Renovate partagé.

### Évolutions techniques
- Intégration de la validation automatique du preset dans le pipeline CI pour prévenir les erreurs de configuration.
- Alignement de la configuration Renovate avec les paramètres Dependabot existants pour assurer une cohérence entre les outils de mise à jour. [#2](https://github.com/proconnect-gouv/renovate-config/pull/2)
- Ajout d'une contrainte de version pour le SDK Sentry (limitation aux versions inférieures à la v11) dans le preset Scalingo afin d'éviter des incompatibilités. [#3](https://github.com/proconnect-gouv/renovate-config/pull/3)

### Autres changements
- Initialisation du dépôt et de la structure du projet.
