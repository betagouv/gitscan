## Changelog : Docurba (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, Docurba a connu des améliorations significatives tant au niveau de l'interface utilisateur que de l'architecture backend. Des corrections ont été apportées pour améliorer la navigation et la gestion des utilisateurs. Des efforts ont également été déployés pour optimiser les tests et la gestion des données, notamment en ce qui concerne les procédures urbanistiques et les communes. Une nouvelle application interne (internal_api) a été créée et l'authentification a été revue.

### Évolutions fonctionnelles
- Amélioration de la navigation : le département sélectionné est maintenant conservé lors des changements de filtres [#1868](https://github.com/MTES-MCT/Docurba/issues/1868).
- Authentification : remplacement des boutons d'authentification dans l'en-tête par un menu déroulant utilisateur, avec déplacement du bouton "Tableau de bord" hors du menu.
- Redirection après récupération de mot de passe : l'utilisateur est redirigé vers le tableau de bord après avoir cliqué sur le lien de récupération de mot de passe.
- Administration Django : la colonne `soft_delete` des procédures est maintenant éditable.
- Exposition de données : les thèmes des procédures sont maintenant exposés dans l'API SCoT et l'API des communes.
- Ajout d'un champ `started_before_huwart_law` pour indiquer si une procédure a débuté avant la loi Huwart.
- Ajout d'un type d'enum pour les procédures.

### Évolutions techniques
- Création d'une nouvelle application Django `internal_api`.
- Intégration de DRF (Django REST Framework).
- Utilisation de FactoryBoy pour la création d'objets de test.
- Refonte de la gestion des migrations et des index dans Django pour améliorer la robustesse et la performance.
- Utilisation de venv pour la gestion des environnements virtuels.
- Amélioration des tests de l'API SCoT.
- Mise à jour des dépendances : Django (6.0.4 -> 6.0.5), urllib3 (2.6.3 -> 2.7.0), pre-commit (4.5.1 -> 4.6.0), ruff (0.15.11 -> 0.15.12), pytest (9.0.2 -> 9.0.3), django-debug-toolbar (6.2.0 -> 6.3.0).
- Optimisation de la configuration du Makefile.
- Correction de problèmes de mémoire dans les applications de revue.

### Autres changements
- Documentation : mise à jour de la documentation de l'API Nuxt pour inclure les thèmes des communes et des SCoT.
- Amélioration de la gestion des erreurs dans les tests.
- Correction de tests flakys.
- Ajout de `CommuneType TextChoice`.
- Mise à jour du README.
