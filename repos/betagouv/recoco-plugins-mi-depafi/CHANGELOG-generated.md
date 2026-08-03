## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des réalisations, notamment l'ajout de détails enrichis, la gestion des droits d'accès et l'importation de données depuis d'autres sources. Des améliorations de l'interface utilisateur ont également été apportées, notamment pour la présentation des informations et la navigation.

### Évolutions fonctionnelles
- **Détails des réalisations:** Ajout d'informations détaillées sur les réalisations, incluant des partenaires, des projets associés, des photos, des documents et des chiffres clés. [#44](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/44)
- **Gestion des droits:** Seul l'auteur d'une réalisation peut la modifier ou la supprimer.
- **Import de données:** Implémentation d'une fonctionnalité d'import de données depuis Lakaa, incluant les utilisateurs, les projets, les ressources et les réalisations. [#31](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/31), [#33](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/33)
- **Formulaire de réalisation:**
    - Ajout d'un champ obligatoire pour le site web de la réalisation. [#43](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/43)
    - Ajout d'un sélecteur de recherche pour faciliter la sélection des éléments dans le formulaire. [#37](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/37)
    - Amélioration de l'affichage et de la gestion des images dans le formulaire.
- **Liste des réalisations:** Possibilité de modifier l'ordre de tri des réalisations dans la liste. [#39](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/39)
- **Notifications:** Ajout de notifications pour les nouveaux projets et réalisations, y compris des digests pour le personnel. [#34](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/34), [#29](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/29)
- **Suivi CRM:** Ajout d'un suivi des actions (création, suppression) sur les réalisations. [#38](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/38)

### Évolutions techniques
- **Refactoring CSS:** Amélioration de la structure et de la maintenabilité du code CSS.
- **Optimisation des requêtes:** Préchargement des données associées pour améliorer les performances.
- **Gestion des erreurs:** Amélioration de la gestion des erreurs et des exceptions.
- **Tests:** Ajout et amélioration des tests unitaires et d'intégration.
- **Architecture:** Refactorisation de la gestion des icônes de sous-titres.
- **Migration:** Préparation des migrations pour supporter les nouvelles fonctionnalités.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour refléter les dernières évolutions.
- **Nettoyage du code:** Suppression de code inutile et amélioration de la lisibilité du code.
- **Amélioration de l'interface utilisateur:** Ajustements de style et d'ergonomie pour améliorer l'expérience utilisateur.
- **Correction de bugs:** Correction de divers bugs et problèmes mineurs.
- **Gestion des permissions:** Ajout d'une gestion des permissions pour les réalisations.
- **Amélioration de la gestion des images:** Optimisation de la gestion des images et des photos.
- **Ajout d'un switch feature:** Ajout d'un mécanisme de switch pour activer/désactiver certaines fonctionnalités. [#30](https://github.com/betagouv/recoco-plugins-mi-depafi/pulls/30)
