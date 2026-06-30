## Changelog : Docurba (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'authentification avec l'intégration de Supabase, la refonte de l'architecture backend avec l'utilisation de Nginx et l'optimisation des performances de l'API interne. De nombreuses améliorations ont également été apportées à l'interface utilisateur, notamment sur les pages de procédures et de collectivités, ainsi qu'un nettoyage important de composants inutilisés.

### Évolutions fonctionnelles
- **Authentification :** Intégration de l'authentification via Supabase, incluant la gestion des sessions et l'ajout d'un champ `last_sign_in_at` dans le modèle User. [#9b990ef](https://github.com/MTES-MCT/Docurba/commit/9b990ef)
- **Interface utilisateur :**
    - Amélioration de la gestion des événements et des procédures sur les pages dédiées, avec affichage des dates de procédure. [#0954b31](https://github.com/MTES-MCT/Docurba/commit/0954b31)
    - Correction de bugs et améliorations de l'expérience utilisateur sur la page "Mes collectivités". [#acca044](https://github.com/MTES-MCT/Docurba/commit/acca044)
    - Possibilité de modifier les événements directement depuis l'interface d'administration Django.
    - Ajout de filtres pour la recherche de collectivités et de communes via l'API interne.
- **Administration Django :**
    - Ajout de la possibilité de rechercher des utilisateurs par email dans l'interface d'administration.
    - Mise à jour du mot de passe des utilisateurs via l'interface d'administration.
    - Exposer les champs `owner_id` et `from_sudocuh` des procédures dans l'interface d'administration.
    - Ajout de la gestion des événements dans l'interface d'administration.
- **API Interne :**
    - Pagination des résultats de l'API interne.
    - Filtrage par département, région et type de juridiction.

### Évolutions techniques
- **Infrastructure :**
    - Remplacement de `wget` par `curl`. [#f040adc](https://github.com/MTES-MCT/Docurba/commit/f040adc)
    - Configuration de Nginx pour servir les fichiers statiques et ajouter une limitation de débit. [#dcb5c6e](https://github.com/MTES-MCT/Docurba/commit/dcb5c6e)
    - Suppression de la dépendance `whitenoise` et `django-revproxy`.
- **Backend :**
    - Utilisation explicite de la variable d'environnement `DOCURBA_API_URL` dans Nuxt. [#bcaf256](https://github.com/MTES-MCT/Docurba/commit/bcaf256)
    - Amélioration de la performance du modèle Event.
    - Harmonisation de la gestion des paramètres de requête dupliqués dans l'API interne.
    - Refonte de la modélisation des événements pour une meilleure cohérence avec la production.
- **Tests :**
    - Ajout de tests pour l'API.
    - Amélioration de la performance des tests Django.
    - Ajout d'un client staff pour les tests.
- **Dépendances :**
    - Mise à jour de plusieurs dépendances : `pytest`, `ruff`, `cryptography`, `pyjwt`, `django-filter`, `supabase`.

### Autres changements
- Suppression de nombreux composants inutilisés (Stats*, Frise*, Charts*, V*, Record* etc.).
- Suppression de fichiers d'assets inutilisés (FRA_*, pcaet-topo.json, etc.).
- Nettoyage du code et suppression de commentaires inutiles.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un système d'alerte Slack lors des déploiements.
- Historisation des modifications d'événements.
- Amélioration de la configuration des templates.
- Correction de l'affichage des événements de prescription.
- Ajout de catégories PAC dans Django.
- Correction de l'initialisation de la sélection de section trame.
