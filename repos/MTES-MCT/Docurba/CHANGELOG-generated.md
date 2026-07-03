## Changelog : Docurba (30 derniers jours, au 02 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la gestion des événements et des procédures, notamment dans l'interface Nuxt3. Des corrections ont été apportées pour une meilleure détection des événements, une gestion plus précise des dates et une intégration plus robuste avec l'API Django. Des optimisations de performance et des corrections de sécurité ont également été implémentées, ainsi que des refactorings importants pour améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration de la détection des événements de lancement et correction des messages d'erreur associés dans l'interface Nuxt3. [#3319000](https://github.com/MTES-MCT/Docurba/issues/3319000)
- Ajout des dates de procédure sur les pages "Procédures" et "Collectivités" dans Nuxt3. [#0954b31](https://github.com/MTES-MCT/Docurba/issues/0954b31)
- Application du nom et de l'email de l'utilisateur comme auteur de commit lors de la mise à jour des PACs dans Nuxt3. [#29296c3](https://github.com/MTES-MCT/Docurba/issues/29296c3)
- Ajout de l'ID de la procédure dans l'onglet "Procédures et Validations". [#53de844](https://github.com/MTES-MCT/Docurba/issues/53de844)
- Ajout de nouvelles catégories de PAC dans Django. [#a553a34](https://github.com/MTES-MCT/Docurba/issues/a553a34)
- Ajout d'une nouvelle catégorie d'événements dans Django. [#a26bfc2](https://github.com/MTES-MCT/Docurba/issues/a26bfc2)
- Historisation de toutes les modifications d'événements. [#cfb4754](https://github.com/MTES-MCT/Docurba/issues/cfb4754)
- Limitation des champs envoyés dans les payloads des webhooks. [#bb02643](https://github.com/MTES-MCT/Docurba/issues/bb02643)
- Ajout de la possibilité de rechercher des événements de prescription. [#13efcf1](https://github.com/MTES-MCT/Docurba/issues/13efcf1)
- Application de la loi Huwart à toutes les procédures dans Nuxt3. [#bcac074](https://github.com/MTES-MCT/Docurba/issues/bcac074)
- Correction du tri des procédures par date dans Nuxt3. [#e0c83d6](https://github.com/MTES-MCT/Docurba/issues/e0c83d6)

### Évolutions techniques
- Mise en place d'un reverse proxy Nginx pour améliorer la sécurité et les performances. [#dcb5c6e](https://github.com/MTES-MCT/Docurba/issues/dcb5c6e)
- Suppression de la dépendance Whitenoise et configuration de Nginx pour servir les fichiers statiques. [#dcb5c6e](https://github.com/MTES-MCT/Docurba/issues/dcb5c6e)
- Intégration de l'authentification Supabase. [#9b990ef](https://github.com/MTES-MCT/Docurba/issues/9b990ef)
- Ajout d'un modèle Session et de sa factory. [#e4364f2](https://github.com/MTES-MCT/Docurba/issues/e4364f2)
- Ajout du header HTTP `Supabase-Authorization`. [#aeed41e](https://github.com/MTES-MCT/Docurba/issues/aeed41e)
- Refactorisation de l'architecture Django pour une meilleure gestion des événements et des procédures.
- Optimisation des performances des requêtes Django.
- Suppression de composants inutilisés dans l'interface Nuxt3.
- Suppression de fichiers d'assets inutilisés.
- Mise à jour des dépendances : Django, pytest, ruff, django-debug-toolbar, django-environ, cryptography, pyjwt, django-filter, supabase.
- Correction d'une erreur 500 due à une annotation manquante dans Django. [#48acd28](https://github.com/MTES-MCT/Docurba/issues/48acd28)
- Ajout de l'environnement aux paramètres Django. [#b3a4d64](https://github.com/MTES-MCT/Docurba/issues/b3a4d64)
- Suppression de commandes de gestion obsolètes. [#fa0ac1d](https://github.com/MTES-MCT/Docurba/issues/fa0ac1d)

### Autres changements
- Ajout d'une alerte Slack lors du lancement d'un déploiement. [#6209a5c](https://github.com/MTES-MCT/Docurba/issues/6209a5c)
- Ajout du champ `last_sign_in_at` au modèle User. [#fff6e6f](https://github.com/MTES-MCT/Docurba/issues/fff6e6f)
- Ajout de commentaires dans le code pour une meilleure compréhension.
- Correction de la configuration des templates. [#863748b](https://github.com/MTES-MCT/Docurba/issues/863748b)
- Ajout d'une variable d'environnement `DEBUG_SQL` pour activer le logging des requêtes SQL. [#9a1f36a](https://github.com/MTES-MCT/Docurba/issues/9a1f36a)
- Suppression d'une réversion précédente du fichier `.gitignore`. [#62c4eeb](https://github.com/MTES-MCT/Docurba/issues/62c4eeb)
