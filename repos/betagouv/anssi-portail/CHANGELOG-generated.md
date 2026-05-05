## Changelog : anssi-portail (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des guides et de la sécurité. Des mises à jour importantes ont été apportées à l'interface utilisateur avec l'adoption de composants DSFR, ainsi que des corrections de bugs et des améliorations de la sécurité, notamment la validation des entrées et la mise à jour des dépendances. L'ajout de la gestion de la langue anglaise pour le contenu NIS2 est également une nouveauté significative.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger la documentation NIS2. [#1234](https://github.com/betagouv/anssi-portail/issues/1234)
- Implémentation d'une recherche d'entreprise (en développement).
- Amélioration de l'affichage des cartes dans le catalogue et les solutions.
- Ajout d'un sélecteur de langue pour le contenu NIS2, permettant d'afficher le contenu en anglais.
- Copie du lien court des guides dans le presse-papier.
- Affichage des documents associés aux guides dans l'interface d'administration.
- Possibilité de supprimer des documents associés à un guide depuis l'interface d'administration.
- Correction de l'indication des filtres actifs dans la section "Financement".
- Correction de la désactivation du bouton.
- Amélioration de la gestion des entités HTML dans les titres des cartes.
- Correction de certaines validations Zod dans la section "SOIN".
- Correction de l'affichage des images dans le test de maturité.

### Évolutions techniques
- Mise à jour de la librairie d'interface utilisateur UIKIT en version 1.49.0.
- Migration vers les composants DSFR pour les boutons, les liens, les cartes et les accordéons.
- Refonte du composant bouton en Svelte 5.
- Utilisation de Zod pour la validation des entrées, remplaçant express-validator.
- Amélioration du typage des objets validés.
- Mise à jour de plusieurs dépendances de sécurité (dompurify, fast-xml-parser, uuid, postcss, follow-redirects).
- Mise à jour de Sentry en version 10.
- Ajout d'une règle ESLint pour vérifier l'utilisation de la validation de schéma dans les routes.
- Suppression de la notion de nonce pour la sécurité.
- Ajout de sourcemaps pour Sentry.
- Amélioration de la gestion des secrets et des variables d'environnement.
- Utilisation de la dernière version de la carte DSFR.

### Autres changements
- Ajout de tests unitaires avec Vitest.
- Amélioration de la documentation.
- Nettoyage du code et suppression de code inutile.
- Correction de l'effet d'étirement des SVG.
- Ajout d'attributs alt aux images pour l'optimisation SEO.
- Ajout de meta descriptions aux URL manquantes pour l'optimisation SEO.
- Harmonisation des cellules ISO dans le module NIS2.
- Ajout de la référence ISO dans le badge NIS2.
- Mise à jour du nombre de services cyber consultés.
- Correction de la lecture des guides.
- Suppression d'une branche inutile.
- Initialisation des descriptions de sous-module.
- Ajout de la gestion de l'export CSV en anglais.
- Correction de l'accès aux variables d'environnement.
- Amélioration de la gestion des erreurs et des alertes.
- Ajout de la trace des clics sur les liens.
- Suppression de l'aseptisation du middleware.
- Suppression de l'ancien style des favoris.
- Suppression de l'ancien accordéon.
- Ajout de la gestion du gap des cartes.
- Ajout de la gestion du wrapper Bouton.
- Correction de l'affichage du séparateur sur fond blanc.
- Ajout de la possibilité de lire les secrets.
- Ajout de la gestion de la langue dans le nom du fichier exporté.
- Ajout de la gestion des rôles.
- Ajout de la gestion des documents dans les guides.
- Ajout de la gestion de l'ajout de documents dans les guides.
- Ajout de la gestion de la suppression de documents dans les guides.
- Amélioration de la gestion des erreurs.
- Ajout de la gestion de l'affichage des documents associés aux guides.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la copie du lien court des guides dans le presse-papier.
- Ajout de la gestion de l'affichage des documents associés aux guides.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
- Ajout de la gestion de la suppression de documents associés aux guides.
- Ajout de la gestion de la vérification de l'existence du fichier avant de l'ajouter.
