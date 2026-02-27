## Changelog : conversations (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un mode sombre persistant, la gestion des pièces jointes et l'optimisation de l'interface. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant l'affichage des messages en mode sombre, les types de fichiers et les traductions. Des améliorations techniques ont été réalisées pour optimiser les performances et la maintenance du code.

### Évolutions fonctionnelles
- Possibilité de désactiver la recherche internet automatique pour l'utilisateur. (#4545083)
- Amélioration de la gestion des pièces jointes avec correction du type MIME pour les fichiers PPTX. (#1088d88)
- Ajout d'un mode sombre persistant, conservant le thème choisi par l'utilisateur. (#ff9e833)
- Implémentation de FindRagBackend pour une meilleure intégration de la recherche. (#23fa1d6)
- Amélioration de l'intégration de l'API Find avec les informations de l'utilisateur et les tags. (#3106d5f)
- Ajout d'un kit d'interface utilisateur (UI Kit) avec support du mode sombre. (#c231e69)
- Possibilité d'utiliser le stockage S3 sans accès externe. (#853305a)
- Ajout d'un bouton de copie pour le code.
- Ajout d'outils RAG génériques pour la recherche.

### Évolutions techniques
- Refactorisation du service AIAgentService pour une meilleure lisibilité et maintenabilité. (#ba712af)
- Migration de ESLint vers la version 9 avec une configuration plate. (#9935335)
- Mise à jour de plusieurs dépendances : Django, pydantic-ai, pillow, django-pydantic-field, pypdf. (#8feed1e, #61f86e1, #224e6f8)
- Optimisation du rendu Markdown en streaming avec une division en blocs. (#af6facf)
- Utilisation de `uv` au lieu de `pip` pour Crowdin. (#e925bff)
- Migration vers `uv` pour une meilleure performance. (#ab2ad03)
- Correction de l'ordre de liveness et readiness dans les déploiements Helm. (#e60c938)
- Amélioration de la gestion des types de données pour les collections. (#c87c734)
- Refactorisation des parsers de documents. (#1c573ad)
- Optimisation de la taille du bundle de surlignage de syntaxe. (#23964cb)

### Autres changements
- Mise à jour des chaînes de traduction. (#a919d9a)
- Publication d'une nouvelle version (0.0.13). (#9506df3)
- Correction de bugs mineurs liés à l'affichage des messages en mode sombre, aux formules mathématiques et aux traductions de la carrousel. (#2b81234, #09dceb5)
- Correction de l'ignorance de la casse lors de la restauration par email. (#3c3eaf3)
- Vendorisation du fichier mime.types pour une meilleure gestion des types de fichiers. (#63e0e6c)
- Suppression de code mort et de fichiers inutilisés.
- Ajustement temporaire du tableau. (#5d895d1)
- Masquage du "waffle" si le thème n'est pas français. (#96a2963)
- Correction de l'affichage des boutons en mode sombre. (#8ed72fb)
- Suppression de l'exécution de Trivy sur yarn.lock pour la génération de mails. (#fb297b9)
- Mise à jour de la version de Next.js et Protobuf. (#7858476, #c02254e)
