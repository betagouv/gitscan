## Changelog : potentiel (30 derniers jours, au 2026-04-22)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des documents, l'ajout de nouveaux rôles utilisateurs, la correction de bugs et l'optimisation de l'expérience utilisateur, notamment au niveau des garanties financières et des notifications. Des améliorations techniques ont également été apportées pour faciliter le développement et la maintenance du projet.

### Évolutions fonctionnelles

*   **Rôles utilisateurs :** Ajout d'un nouveau rôle "admin" (anciennement DGEc) pour une gestion des permissions plus précise. [#4183](https://github.com/MTES-MCT/potentiel/issues/4183)
*   **Garanties financières :** Refonte complète des pages de gestion des garanties financières pour une meilleure ergonomie. [#4175](https://github.com/MTES-MCT/potentiel/issues/4175)
*   **Notifications :** Correction d'un bug empêchant l'envoi de notifications de rappel aux GRD. [#4180](https://github.com/MTES-MCT/potentiel/issues/4180)
*   **Accessibilité :** Amélioration de l'accessibilité des listes (réclamations, documents, utilisateurs) avec l'ajout de liens ARIA. [#4186](https://github.com/MTES-MCT/potentiel/issues/4186)
*   **Valeurs par défaut :** Intégration des valeurs par défaut pour le coefficient K. [#4160](https://github.com/MTES-MCT/potentiel/issues/4160)
*   **Achèvement :** Ajout d'un bloc d'information lors de l'achèvement d'une étape. [#4132](https://github.com/MTES-MCT/potentiel/issues/4132)
*   **Copie ID projet :** Possibilité pour les utilisateurs DREALS de copier l'identifiant du projet en production. [#4151](https://github.com/MTES-MCT/potentiel/issues/4151)
*   **Import données :** Import des références de raccordement (DN) et des données de la région. [#4103](https://github.com/MTES-MCT/potentiel/issues/4103), [#4153](https://github.com/MTES-MCT/potentiel/issues/4153)

### Évolutions techniques

*   **Refactoring :** Simplification de la modélisation des Autorisations d'Opérer (AO). [#4147](https://github.com/MTES-MCT/potentiel/issues/4147)
*   **Types de données :** Uniformisation et amélioration des types de données pour les documents (Délai, Actionnaire, Dispositif de Stockage, Représentant Légal, Installateur, Fournisseur, Achèvement, Recours, etc.). [#4119](https://github.com/MTES-MCT/potentiel/issues/4119), [#4124](https://github.com/MTES-MCT/potentiel/issues/4124), [#4121](https://github.com/MTES-MCT/potentiel/issues/4121), [#4126](https://github.com/MTES-MCT/potentiel/issues/4126)
*   **Tests :** Implémentation des tests manquants pour les fonctionnalités Délai et Recours. [#4182](https://github.com/MTES-MCT/potentiel/issues/4182)
*   **Cache GraphQL :** Mise en place d'un cache GraphQL pour améliorer les performances.
*   **CI/CD :** Désactivation de l'envoi d'emails pendant les phases de CI. [#4138](https://github.com/MTES-MCT/potentiel/issues/4138)
*   **Storybook :** Correction de build pour storybook et passage à vite. [#4108](https://github.com/MTES-MCT/potentiel/issues/4108)

### Autres changements

*   **Documentation :** Mise à jour des données de test. [#4181](https://github.com/MTES-MCT/potentiel/issues/4181)
*   **Nettoyage de code :** Suppression de scripts obsolètes et simplification du code.
*   **Corrections de bugs :** Plusieurs corrections de bugs mineurs concernant l'affichage, l'import de données et la modification de documents.
*   **Mise à jour des dépendances :** Mises à jour de dépendances (dompurify, picomatch, basic-ftp).
*   **Suppression notification étapes :** Suppression de la notification des étapes du projet en cas de recours. [#4179](https://github.com/MTES-MCT/potentiel/issues/4179)
*   **Harmonisation badges :** Harmonisation des marges des badges. [#4129](https://github.com/MTES-MCT/potentiel/issues/4129)
