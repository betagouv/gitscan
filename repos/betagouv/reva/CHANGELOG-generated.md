## Changelog : reva (30 derniers jours, au 30 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur, notamment autour de l'intégration de FranceConnect et de la gestion des candidatures. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des refactorings techniques pour améliorer la maintenabilité du code. Un effort particulier a été fait pour améliorer la gestion des erreurs et fournir des messages plus clairs aux utilisateurs.

### Évolutions fonctionnelles
- **FranceConnect :** Amélioration significative de l'intégration de FranceConnect, avec une gestion plus robuste des erreurs et des informations utilisateur. Ajout de pages de nettoyage pour les données de test FranceConnect.
- **Gestion des candidatures :**
    - Ajout de la possibilité d'abandonner une candidature si le dossier de recevabilité n'a pas été envoyé.
    - Amélioration du flux d'abonnement aux AAP avec des alertes et des vérifications du SIRET.
    - Possibilité de supprimer une candidature en cours de projet.
    - Ajout de la gestion de l'archivage des candidatures.
- **Administration :**
    - Refonte de la page de gestion des dates de jury, avec une meilleure réactivité.
    - Amélioration de l'interface de gestion des résultats de jury, avec affichage par blocs de compétences.
    - Ajout d'une page pour gérer les comptes locaux des administrateurs.
    - Ajout de la possibilité de masquer les certifications expirées.
- **VAE Collective :** Suppression de l'URL avec code de la page cohorte.
- **Interface utilisateur :** Amélioration de l'affichage des informations de la ville et du département dans les formulaires d'adresse.

### Évolutions techniques
- **Refactoring :**
    - Refactorisation du code d'authentification pour améliorer la sécurité et la maintenabilité.
    - Suppression de code obsolète lié à d'anciennes fonctionnalités.
    - Simplification de la logique de vérification des décisions.
    - Organisation des routes de l'administration en groupes publics et privés.
- **Performances :** Ajout d'index sur les tables de la base de données pour améliorer les performances des requêtes.
- **Tests :** Ajout et mise à jour de nombreux tests unitaires et d'intégration.
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment `fastify`, `lodash`, `@graphql-codegen/*` et `vite`.
- **Sécurité :** Amélioration de la sécurité en vérifiant l'ID client et le champ `aud` du JWT pour atténuer les attaques de type "confused deputy".

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Suppression de tables de base de données inutilisées.
- Amélioration des messages d'erreur et des journaux.
- Ajustements de style et de mise en page.
- Correction de problèmes de compatibilité avec les navigateurs.
- Ajout de commentaires et de documentation au code.
- Suppression de feature flags obsolètes.
