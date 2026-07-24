## Changelog : eva-serveur (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des évaluations, notamment une séparation claire entre les évaluations EVA et Evaprogramme, ainsi que des corrections de bugs et des optimisations de l'interface utilisateur. L'accès aux campagnes Evaprogramme a été restauré en lecture.

### Évolutions fonctionnelles
- Restauration de l'accès en lecture aux campagnes Evaprogramme. [#ba5c0f2](https://github.com/betagouv/eva-serveur/commit/ba5c0f2)
- Affichage du nom du bénéficiaire des évaluations. [#f35d8f5](https://github.com/betagouv/eva-serveur/commit/f35d8f5)
- Correction du message d'accueil pour les comptes en attente. [#1eaf69d](https://github.com/betagouv/eva-serveur/commit/1eaf69d)
- Ajout de redirections pour l'ancienne route `admin_evaluations_path`. [#ccffb9d](https://github.com/betagouv/eva-serveur/commit/ccffb9d)
- Correction de typographies dans les noms de structures. [#bf1d7d5](https://github.com/betagouv/eva-serveur/commit/bf1d7d5)
- Création d'un menu "Evaluation" avec des sections distinctes pour EVA et Evaprogramme, accessible aux super-administrateurs. [#eda543b](https://github.com/betagouv/eva-serveur/commit/eda543b)
- Création de la page "EvaluationEvapro" et de son export PDF. [#9539b7f](https://github.com/betagouv/eva-serveur/commit/9539b7f) et [#2c2ca7f](https://github.com/betagouv/eva-serveur/commit/2c2ca7f)
- Correction du formulaire de modification d'une évaluation. [#39044c4](https://github.com/betagouv/eva-serveur/commit/39044c4)
- Correction d'un bug empêchant l'inscription sans proposition de rejoindre des structures administratives. [#b123c23](https://github.com/betagouv/eva-serveur/commit/b123c23)

### Évolutions techniques
- Refactorisation de la bannière "solution illettrisme" en composant réutilisable. [#5be2e61](https://github.com/betagouv/eva-serveur/commit/5be2e61)
- Création des modèles `EvaluationEva` et `EvaluationEvapro` pour séparer les types d'évaluations. [#3bbc730](https://github.com/betagouv/eva-serveur/commit/3bbc730)
- Factorisation du code et suppression de duplications dans les sidebars. [#deed0f2](https://github.com/betagouv/eva-serveur/commit/deed0f2), [#9d34beb](https://github.com/betagouv/eva-serveur/commit/9d34beb), [#9b6c5f2](https://github.com/betagouv/eva-serveur/commit/9b6c5f2)
- Renommage et déplacement de fichiers et partials pour une meilleure organisation. [#7a7ffcd](https://github.com/betagouv/eva-serveur/commit/7a7ffcd), [#631d54a](https://github.com/betagouv/eva-serveur/commit/631d54a), [#d99ae2a](https://github.com/betagouv/eva-serveur/commit/d99ae2a)
- Suppression de code mort et de constantes dupliquées. [#4a6ca25](https://github.com/betagouv/eva-serveur/commit/4a6ca25), [#47c35ff](https://github.com/betagouv/eva-serveur/commit/47c35ff)
- Amélioration de la gestion des autorisations sur les modèles. [#284f120](https://github.com/betagouv/eva-serveur/commit/284f120)
- Correction de bugs liés à l'import de questions et à la recherche de parties. [#b18d7a8](https://github.com/betagouv/eva-serveur/commit/b18d7a8), [#5aeb734](https://github.com/betagouv/eva-serveur/commit/5aeb734)
- Correction d'un crash lors de l'import avec de nombreuses erreurs. [#b18d7a8](https://github.com/betagouv/eva-serveur/commit/b18d7a8)

### Autres changements
- Correction de plusieurs `rubocop_todo`. [#01508ad](https://github.com/betagouv/eva-serveur/commit/01508ad) et [#7daeb28](https://github.com/betagouv/eva-serveur/commit/7daeb28)
- Amélioration du style de la modale d'invitation. [#581cfeb](https://github.com/betagouv/eva-serveur/commit/581cfeb)
- Correction de la traduction d'une erreur de génération de PDF. [#1fb9500](https://github.com/betagouv/eva-serveur/commit/1fb9500)
- Suppression de l'accès au compte Evaprogramme pour le modèle Campagne. [#f53a328](https://github.com/betagouv/eva-serveur/commit/f53a328)
- Mise à jour des dépendances (view_component, dsfr-view-components). [#c6d05d6](https://github.com/betagouv/eva-serveur/commit/c6d05d6) et [#d6ec975](https://github.com/betagouv/eva-serveur/commit/d6ec975)
- Amélioration de l'interface utilisateur pour éviter le défilement horizontal sur les tableaux. [#4a0885a](https://github.com/betagouv/eva-serveur/commit/4a0885a)
