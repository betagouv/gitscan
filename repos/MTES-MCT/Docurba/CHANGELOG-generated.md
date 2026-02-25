## Changelog : Docurba (30 derniers jours)

### Résumé
Cette période a été marquée par une importante mise à niveau de la version de Django, ainsi que par de nombreuses améliorations de l'interface utilisateur et de la gestion des données, notamment au niveau de l'administration des procédures et des enquêtes. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Les administrateurs peuvent désormais voir les événements sur la page de modification d'une procédure. (#225c624)
- Amélioration de l'affichage des informations de périmètre des procédures dans l'interface d'administration. (#33307e5, #2b69ad2)
- Correction des tris sur la page "Mes procédures" dans l'interface Nuxt. (#8f9b688)
- Affichage du label "(PPA)" après le poste dans l'interface Nuxt. (#e6d3c8f)
- Les événements structurants Sudocuh sont maintenant reconnus par Docurba. (#8a1441b)
- Les administrateurs peuvent voir le statut de la procédure (Nuxt) et le statut (Django) dans l'interface d'administration. (#225c624)
- Les enquêtes sont désactivées pour les DDT qui ne sont pas présentes dans la liste `DDT_ENQUETE_ENABLED`. (#6426634)
- L'édition de l'email est désactivée dans l'interface d'administration. (#600cfe5)
- Ajout de code état et de filtres "avant" à la page de débogage des collectivités. (#317dcb0)
- Redirection vers la page de la collectivité après une connexion réussie. (#027a6b1)
- Correction d'un bug empêchant l'ouverture de la page de modification d'une procédure. (#5be0a6b)
- Correction d'un bug lors de l'affichage du statut de la procédure dans l'interface d'administration. (#33307e5)
- Amélioration de la description de la liste des DU sur les pages des collectivités. (#c525cae)

### Évolutions techniques
- Mise à niveau de Django de la version 5.2.11 à la version 6.0.2. (#48cd3f1)
- Refonte de la configuration pre-commit. (#82ea75a)
- Transformation des logs en format JSON pour Datadog. (#38e46e8)
- Correction de problèmes de requêtes N+1 sur les appels API et dans l'interface d'administration. (#b9a67a7, #b602b16, #66f55c9)
- Mise à jour de l'URL d'autorisation pour le magic link Supabase, chargée depuis une variable d'environnement. (#f7129d8)
- Utilisation de `avant` pour déterminer la caducité lors de l'export SCoT. (#8ae61c9)
- Mise à jour de plusieurs dépendances : `ruff`, `pytest-django`, `django-environ`, `sqlparse`, `django-browser-reload`, `pre-commit`, `ptpython`.

### Autres changements
- Ajout d'usines pour générer de faux objets pour les tests. (#9bfe2a7)
- Réusinage avec utilisation des usines. (#6b2f382)
- Amélioration de la documentation de l'API avec des exemples utilisant `avant=2026-01-01`. (#0d8df07)
- Ajout d'un cooldown de 7 jours pour Dependabot. (#974e754)
- Correction d'une erreur 500 dans l'interface d'administration. (#b6744d7)
- Affichage d'une page 404 au lieu d'une 500 en cas d'erreur. (#2fdde59)
- Correction d'une erreur de linter dans Nuxt. (#61503d0)
- Rafraîchissement du formulaire de connexion même en cas d'erreur. (#c2adf56)
- Correction d'un bug concernant la snackbar de réinitialisation du mot de passe. (#62c0da1)
- Ajout de commentaires et de la colonne `is_principale` au modèle `Procedure`. (#63c6efa, #3169318)
- Ajout de la colonne `commentaire` au modèle `Procedure`. (#68d4cd6)
- Suppression et création de recettes jetables. (#e7b2252)
- Amélioration de l'organisation des imports. (#a55a7e6, #9d52ab6)
- Utilisation du logger root. (#a60361a)
