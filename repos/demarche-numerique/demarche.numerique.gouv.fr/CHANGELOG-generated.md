## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des pièces justificatives, la personnalisation des dossiers et l'intégration de nouvelles données (quotient familial, données ARS). Des optimisations de performance et des corrections de bugs ont également été apportées, ainsi que des améliorations de la sécurité et de la maintenance technique.

### Évolutions fonctionnelles
- **API Part:** Intégration des données Quotient Familial et ARS, avec la possibilité de rafraîchir les données pour le Quotient Familial.
- **Dossiers:**
    - Amélioration de la gestion des pièces justificatives (ajout, suppression, affichage).
    - Possibilité pour les instructeurs de modifier les dossiers (avec une notification pour l'utilisateur).
    - Affichage du statut de lecture des messages dans la messagerie pour tous les instructeurs du groupe.
    - Ajout d'un indicateur de lecture des messages dans la messagerie.
- **Personnalisation:** Amélioration de l'écran de personnalisation des dossiers, avec la possibilité de choisir les champs à afficher.
- **Export:** Amélioration de l'export des données en CSV, avec streaming pour réduire la consommation de mémoire.
- **Interface utilisateur:** Amélioration de l'accessibilité et de l'ergonomie de l'interface utilisateur, notamment pour les champs et les boutons.
- **Sécurité:** Ajout d'une validation de la présence d'un token API pour certaines fonctionnalités.
- **Statistiques:** Amélioration du calcul et de l'affichage des statistiques.

### Évolutions techniques
- **Rails 8:** Finalisation de la migration vers Rails 8.
- **GraphQL:** Utilisation de DataLoaders pour optimiser les requêtes GraphQL.
- **Tests:** Ajout et amélioration des tests unitaires et système.
- **Performance:** Optimisations de performance pour les requêtes en base de données et l'export des données.
- **Sécurité:** Renforcement de la sécurité de l'application.
- **Architecture:** Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- **CI/CD:** Amélioration du pipeline CI/CD.
- **Dépendances:** Mise à jour des dépendances.
- **Oaken:** Utilisation de Oaken pour la gestion des données de test.
- **Haml vers ERB:** Migration de plusieurs templates Haml vers ERB.
- **Suppression de code obsolète:** Suppression de code obsolète et de fonctionnalités non utilisées.

### Autres changements
- **Documentation:** Mise à jour de la documentation.
- **i18n:** Extraction de chaînes de caractères en dur pour la traduction.
- **Linting:** Amélioration de la qualité du code grâce à l'utilisation de linters.
- **Accessibilité:** Amélioration de l'accessibilité de l'application.
- **Configuration:** Mise à jour de la configuration de l'application.
- **Nettoyage du code:** Nettoyage du code pour améliorer la lisibilité et la maintenabilité.
