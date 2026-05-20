## Changelog : Docurba (30 derniers jours, au 18 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la gestion des procédures et des données, notamment en lien avec la loi Huwart. Des corrections ont été apportées pour garantir la conformité et la précision des informations. L'interface utilisateur a également été améliorée, avec notamment une refonte du menu utilisateur et des corrections pour une meilleure expérience de navigation. Des efforts ont été faits pour optimiser les tests et l'infrastructure du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la création de PLU avec plusieurs communes. [#9553d70](https://github.com/MTES-MCT/Docurba/commit/9553d70)
- Amélioration de la navigation : le département sélectionné est maintenant conservé lors des changements de page. [#e90940a](https://github.com/MTES-MCT/Docurba/commit/e90940a)
- Redirection automatique vers le tableau de bord après la récupération du mot de passe. [#a089e00](https://github.com/MTES-MCT/Docurba/commit/a089e00)
- Refonte du menu utilisateur : remplacement des boutons d'authentification par un menu déroulant. [#ba90536](https://github.com/MTES-MCT/Docurba/commit/ba90536)
- Le bouton "Tableau de bord" est maintenant accessible directement depuis le menu utilisateur. [#669caf9](https://github.com/MTES-MCT/Docurba/commit/669caf9)
- Amélioration de la synchronisation des champs de recherche avec les paramètres de l'URL. [#ab4cb4d](https://github.com/MTES-MCT/Docurba/commit/ab4cb4d)
- Ajout de la possibilité d'éditer la colonne `soft_delete` de la procédure dans l'interface d'administration Django. [#d7bb24a](https://github.com/MTES-MCT/Docurba/commit/d7bb24a)

### Évolutions techniques
- Refactorisation : déplacement de l'application `internal_api` dans le répertoire `docurba`. [#05af439](https://github.com/MTES-MCT/Docurba/commit/05af439)
- Mise en place de FactoryBoy pour la création d'objets de test. [#2bc0c2a](https://github.com/MTES-MCT/Docurba/commit/2bc0c2a)
- Création de factories pour User, Profile, Procedure et CommuneProcedure. [#0fa8902](https://github.com/MTES-MCT/Docurba/commit/0fa8902), [#3275c81](https://github.com/MTES-MCT/Docurba/commit/3275c81)
- Correction de conflits de migration Django. [#13d2489](https://github.com/MTES-MCT/Docurba/commit/13d2489)
- Ajout d'un index personnalisé `OversizedIndex` pour améliorer les performances des requêtes. [#ef0f970](https://github.com/MTES-MCT/Docurba/commit/ef0f970)
- La colonne `commune_id` de la table `CommuneProcedure` est maintenant générée automatiquement. [#b9c56a3](https://github.com/MTES-MCT/Docurba/commit/b9c56a3)
- La table `CommuneProcedure` est maintenant gérée par Django. [#130c1d9](https://github.com/MTES-MCT/Docurba/commit/130c1d9)
- Ajout d'un champ `type` à la table `Commune` avec un choix de texte. [#6b5ea57](https://github.com/MTES-MCT/Docurba/commit/6b5ea57)
- Utilisation de venv pour la gestion des environnements virtuels. [#b333432](https://github.com/MTES-MCT/Docurba/commit/b333432)
- Suppression de l'activation de l'environnement virtuel dans les tâches de test. [#3962f9c](https://github.com/MTES-MCT/Docurba/commit/3962f9c)
- Mise à jour de la documentation Makefile. [#77a8823](https://github.com/MTES-MCT/Docurba/commit/77a8823)

### Autres changements
- Suppression des événements de fin d'échéance pour se conformer à la loi Huwart. [#62f67e4](https://github.com/MTES-MCT/Docurba/commit/62f67e4)
- Mise à jour du nom de la procédure lors de la mise à jour du type de document. [#5737491](https://github.com/MTES-MCT/Docurba/commit/5737491)
- Distinction du type de collectivité EPCI des autres. [#399bc60](https://github.com/MTES-MCT/Docurba/commit/399bc60)
- Ajout de la possibilité de remplir le champ `started_before_huwart_law` des procédures. [#92c94f3](https://github.com/MTES-MCT/Docurba/commit/92c94f3) et [#6e716bd](https://github.com/MTES-MCT/Docurba/commit/6e716bd)
- Ajout d'un champ pour stocker si une procédure a commencé avant la loi Huwart. [#6f0b594](https://github.com/MTES-MCT/Docurba/commit/6f0b594)
- Documentation du champ `type` des procédures avec un enum `ProcedureType`. [#3815c89](https://github.com/MTES-MCT/Docurba/commit/3815c89)
- Amélioration des tests de l'API SCoT. [#6c38f20](https://github.com/MTES-MCT/Docurba/commit/6c38f20)
- Ajout de noms de routes pour pouvoir utiliser la fonction `reverse`. [#5508b7e](https://github.com/MTES-MCT/Docurba/commit/5508b7e)
- Ajout d'un dossier `exports` avec un fichier `.gitignore` pour ignorer son contenu. [#1df2ab7](https://github.com/MTES-MCT/Docurba/commit/1df2ab7)
- Mise à jour en masse du type de document des procédures de PLU à PLUi. [#0d6cf9a](https://github.com/MTES-MCT/Docurba/commit/0d6cf9a)
- Correction d'un test fragile. [#f9b454a](https://github.com/MTES-MCT/Docurba/commit/f9b454a)
- Augmentation du plan Supabase pour résoudre les erreurs de mémoire récurrentes. [#1ed6e01](https://github.com/MTES-MCT/Docurba/commit/1ed6e01) et [#f208f08](https://github.com/MTES-MCT/Docurba/commit/f208f08)
- Correction de la documentation de l'API pour les communes et les SCoT. [#e28b305](https://github.com/MTES-MCT/Docurba/commit/e28b305)
- Génération du type d'événement à partir de la catégorie d'événement. [#cf5a814](https://github.com/MTES-MCT/Docurba/commit/cf5a814)
- Suppression du message d'erreur "too-many-arguments". [#c508dd2](https://github.com/MTES-MCT/Docurba/commit/c508dd2)
- Correction du premier affichage d'événement côté client. [#d195401](https://github.com/MTES-MCT/Docurba/commit/d195401)
