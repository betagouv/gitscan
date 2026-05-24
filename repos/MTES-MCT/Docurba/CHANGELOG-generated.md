## Changelog : Docurba (30 derniers jours, au 21 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la conformité à la loi Huwart, notamment dans la gestion des procédures et des événements. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, en particulier concernant la navigation, la création de PLU et la gestion des filtres. Des efforts ont été faits pour améliorer la structure du projet et la qualité du code, avec l'introduction de FactoryBoy pour les tests et la refactorisation de certaines parties du code.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création de PLU avec plusieurs communes. [#9553d70](https://github.com/MTES-MCT/Docurba/commit/9553d70)
- Amélioration de la navigation : le département sélectionné est maintenant conservé. [#2a3bcf1](https://github.com/MTES-MCT/Docurba/commit/2a3bcf1)
- Amélioration de la synchronisation des champs de recherche avec les paramètres de l'URL. [#ab4cb4d](https://github.com/MTES-MCT/Docurba/commit/ab4cb4d)
- Redirection automatique vers le tableau de bord après la récupération du mot de passe. [#a089e00](https://github.com/MTES-MCT/Docurba/commit/a089e00)
- La page PAC (Plan d'Aménagement et de Construction) est maintenant accessible publiquement. [#b53a072](https://github.com/MTES-MCT/Docurba/commit/b53a072)
- Correction pour éviter les erreurs liées à des variables non définies. [#df116e1](https://github.com/MTES-MCT/Docurba/commit/df116e1)
- Amélioration du message d'erreur pour les procédures primaires manquantes. [#85e8321](https://github.com/MTES-MCT/Docurba/commit/85e8321)
- Suppression des événements de fin d'échéance pour se conformer à la loi Huwart. [#62f67e4](https://github.com/MTES-MCT/Docurba/commit/62f67e4)

### Évolutions techniques
- Introduction de FactoryBoy pour faciliter la création d'objets de test. [#0fa8902](https://github.com/MTES-MCT/Docurba/commit/0fa8902)
- Refactorisation du code pour déplacer l'application `internal_api` dans le répertoire `docurba`. [#05af439](https://github.com/MTES-MCT/Docurba/commit/05af439)
- Mise à jour de la dépendance `djangorestframework` vers la version 3.17.1. [#696384d](https://github.com/MTES-MCT/Docurba/commit/696384d)
- Mise à jour de la dépendance `django` vers la version 6.0.5. [#c9db28b](https://github.com/MTES-MCT/Docurba/commit/c9db28b)
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0. [#a23dce8](https://github.com/MTES-MCT/Docurba/commit/a23dce8)
- Mise à jour de la dépendance `pre-commit` vers la version 4.6.0. [#7fc1cf4](https://github.com/MTES-MCT/Docurba/commit/7fc1cf4)
- Mise à jour de la dépendance `ruff` vers la version 0.15.12. [#e314adf](https://github.com/MTES-MCT/Docurba/commit/e314adf) et [#fed655a](https://github.com/MTES-MCT/Docurba/commit/fed655a)
- Utilisation d'un environnement virtuel (venv) pour la gestion des dépendances. [#b333432](https://github.com/MTES-MCT/Docurba/commit/b333432)
- Amélioration de la configuration du Makefile. [#77a8823](https://github.com/MTES-MCT/Docurba/commit/77a8823)

### Autres changements
- Ajout de la gestion de `started_before_huwart_law` dans le modèle `Procedure`. [#6f0b594](https://github.com/MTES-MCT/Docurba/commit/6f0b594) et [#92c94f3](https://github.com/MTES-MCT/Docurba/commit/92c94f3)
- Ajout de l'enum `ProcedureType` pour documenter le type de procédure. [#3815c89](https://github.com/MTES-MCT/Docurba/commit/3815c89)
- Modification de la façon dont l'indicateur "i" est affiché. [#359cc55](https://github.com/MTES-MCT/Docurba/commit/359cc55)
- Amélioration des tests de l'API SCoT. [#6c38f20](https://github.com/MTES-MCT/Docurba/commit/6c38f20)
- Ajout de noms de routes pour faciliter l'utilisation de `reverse`. [#5508b7e](https://github.com/MTES-MCT/Docurba/commit/5508b7e)
- Augmentation du plan Supabase et de la taille du disque pour les applications de revue. [#f208f08](https://github.com/MTES-MCT/Docurba/commit/f208f08) et [#1ed6e01](https://github.com/MTES-MCT/Docurba/commit/1ed6e01)
- Correction d'un conflit de migration Django. [#13d2489](https://github.com/MTES-MCT/Docurba/commit/13d2489)
- Déplacement de `TypeCollectivite` vers `core.enums`. [#a9ad3fb](https://github.com/MTES-MCT/Docurba/commit/a9ad3fb)
- Mise à jour du nom de la procédure lors de la mise à jour du type de document. [#5737491](https://github.com/MTES-MCT/Docurba/commit/5737491)
- Distinction des types `EPCI` `TypeCollectivite` des autres. [#399bc60](https://github.com/MTES-MCT/Docurba/commit/399bc60)
- Ajout d'un dossier `exports` et exclusion de son contenu du contrôle de version. [#1df2ab7](https://github.com/MTES-MCT/Docurba/commit/1df2ab7)
- Mise à jour en masse du type de procédure de PLU à PLUi. [#0d6cf9a](https://github.com/MTES-MCT/Docurba/commit/0d6cf9a)
- Déclenchement de l'événement de première vue de la page sur le client. [#d195401](https://github.com/MTES-MCT/Docurba/commit/d195401)
- Rendre la colonne `procedure.soft_delete` éditable dans l'admin Django. [#d7bb24a](https://github.com/MTES-MCT/Docurba/commit/d7bb24a)
- Exposer les sujets des procédures dans l'API SCoT. [#f195396](https://github.com/MTES-MCT/Docurba/commit/f195396) et [#e28b305](https://github.com/MTES-MCT/Docurba/commit/e28b305)
- Générer le type d'événement à partir de `EventCategory`. [#cf5a814](https://github.com/MTES-MCT/Docurba/commit/cf5a814)
- Suppression des erreurs "too-many-arguments". [#c508dd2](https://github.com/MTES-MCT/Docurba/commit/c508dd2)
- Exposer les sujets des procédures dans l'API des communes. [#626398f](https://github.com/MTES-MCT/Docurba/commit/626398f)
- Création de `EventFactory`, `CollectiviteFactory`, `UserFactory`, `ProfileFactory`, `ProcedureFactory` et `CommuneProcedureFactory`. [#c17d417](https://github.com/MTES-MCT/Docurba/commit/c17d417), [#b6c4a1e](https://github.com/MTES-MCT/Docurba/commit/b6c4a1e), [#559bc92](https://github.com/MTES-MCT/Docurba/commit/559bc92), [#2bc0c2a](https://github.com/MTES-MCT/Docurba/commit/2bc0c2a), [#0186c5f](https://github.com/MTES-MCT/Docurba/commit/0186c5f)
