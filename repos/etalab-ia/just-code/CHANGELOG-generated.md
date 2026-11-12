## Changelog : codebox (30 derniers jours, au 11 novembre 2026)

### Résumé
Le projet a franchi une étape majeure avec son rebranding officiel de `just-code` vers **codebox**. Les évolutions récentes se concentrent sur une refonte complète de l'expérience utilisateur, notamment via un nouvel assistant de configuration (wizard) plus intuitif, et sur une amélioration significative de la fiabilité du système pour éviter la perte de données lors des interruptions de session ou des mises à jour.

### Évolutions fonctionnelles
- **Rebranding** : Le projet, son interface en ligne de commande (CLI) et ses chemins de fichiers passent de `just-code` à **codebox**.
- **Assistant de configuration (Wizard)** : Introduction d'un nouveau processus d'initialisation en 5 étapes pour simplifier la configuration initiale (choix des modèles, des compétences et des identifiants).
- **Gestion des modèles** : Support de la sélection multi-modèles et intégration de Ministral comme modèle de petite taille.
- **Gestion des secrets** : Automatisation de l'importation et de l'injection des secrets du projet (fichiers `.dotenv`) directement dans l'environnement d'exécution sécurisé.
- **Continuité de travail** : Amélioration des mécanismes de récupération (recovery) pour préserver les modifications de l'utilisateur et l'état du workspace lors d'une reprise de session ou d'une mise à jour.
- **Interface utilisateur (TUI)** : Amélioration de l'interface en ligne de commande, incluant une meilleure gestion du redimensionnement de la fenêtre et une localisation française plus complète.

### Évolutions techniques
- **Architecture des agents** : Support de "Pi" comme second harnais d'agent ([#176](https://github.com/etalab-ia/just-code/issues/176)).
- **Microsandbox** : Mise à jour du runtime vers la version 0.7.14 et ajout de nouveaux chemins de récupération pour les instances arrêtées après une mise à jour.
- **OpenCode** : Migration vers la version 2.2.5.
- **Statistiques** : Implémentation d'un nouveau système d'envoi des statistiques d'usage vers une table Grist, avec une gestion stricte du consentement de l'utilisateur.
- **Sécurité** : Renforcement de la validation des secrets et durcissement des mécanismes de transport des données entre l'hôte et l'invité.
- **Infrastructure & CI/CD** : Optimisation des pipelines de qualification, notamment pour les architectures macOS et Linux arm64.

### Autres changements
- **Documentation** : Mise à jour importante des guides concernant la gestion des secrets, les processus de qualification et la configuration des environnements.
- **Localisation** : Travail de polissage sur les textes de l'interface en français.
