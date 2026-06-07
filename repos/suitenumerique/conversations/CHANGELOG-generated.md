## Changelog : conversations (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la maintenance et l'ajout de fonctionnalités clés pour la gestion de projets et la surveillance de la santé des modèles d'IA. Des correctifs ont été apportés pour améliorer l'expérience utilisateur, notamment en permettant de taper pendant la génération de réponses par l'IA et en affichant correctement les informations des projets. Une nouvelle fonctionnalité de mode maintenance a également été implémentée.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance planifiées [#fa746ed](https://github.com/suitenumerique/conversations/commit/fa746ed).
- Possibilité de taper pendant que le modèle de langage génère une réponse, améliorant la fluidité de l'interaction [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b).
- Amélioration de l'affichage et du filtrage des chats dans l'interface d'administration [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d).
- Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation) [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2).
- Ajout d'une bannière configurable avec une visibilité limitée dans le temps [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408).
- Nouveau modal de paramètres [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9).

### Évolutions techniques
- Ajout d'une tâche Cron pour surveiller la santé du modèle Albert [#757d75e](https://github.com/suitenumerique/conversations/commit/757d75e) et [#41a591e](https://github.com/suitenumerique/conversations/commit/41a591e).
- Mise à jour des dépendances du backend et du frontend [#3ba131e](https://github.com/suitenumerique/conversations/commit/3ba131e).
- Correction d'un bug dans le déploiement Helm empêchant les pods de respecter le budget de perturbation du backend [#b1f62d6](https://github.com/suitenumerique/conversations/commit/b1f62d6).
- Amélioration de la logique de polling de la santé du modèle [#2536ffa](https://github.com/suitenumerique/conversations/commit/2536ffa).
- Suppression du point de terminaison de la liste des utilisateurs [#ff45878](https://github.com/suitenumerique/conversations/commit/ff45878).
- Désactivation des scripts d'installation Yarn dans le build Docker pour des raisons de sécurité [#119b814](https://github.com/suitenumerique/conversations/commit/119b814).

### Autres changements
- Mise à jour des chaînes de caractères traduites [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101).
- Amélioration de l'instruction pour éviter les hallucinations d'URL [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef).
- Restriction de l'outil d'auto-documentation aux questions concernant les métadonnées [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5).
- Correction d'un bug dans le modal de projet qui ne respectait pas l'indicateur de fonctionnalité de téléchargement de documents [#e4f1d94](https://github.com/suitenumerique/conversations/commit/e4f1d94).
