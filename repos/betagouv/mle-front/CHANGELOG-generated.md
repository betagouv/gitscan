## Changelog : mle-front (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur de nombreuses améliorations pour la plateforme, notamment l'ajout de nouvelles fonctionnalités comme les alertes logement, l'intégration WordPress, et un éditeur WYSIWYG pour les descriptions de logement. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, en particulier au niveau du formulaire de recherche, du tableau de bord et de la gestion des résidences.

### Évolutions fonctionnelles
- Ajout d'un badge indiquant la présence d'une liste d'attente pour les logements.
- Implémentation d'un système d'alertes logement pour les étudiants.
- Intégration de WordPress pour la publication d'annonces et la gestion de contenu.
- Ajout d'un éditeur WYSIWYG pour la description des logements.
- Possibilité de réordonner les photos des logements.
- Ajout d'un indicateur de nombre d'alertes.
- Pagination ajoutée sur le tableau de bord des propriétaires.
- Ajout d'un méga-menu pour une navigation améliorée.
- Possibilité d'ajouter une ville à une annonce.
- Affichage du prix même lorsque le minimum et le maximum sont identiques.
- Ajout d'une fonctionnalité permettant de rediriger l'utilisateur vers la page d'inscription lors de la sauvegarde d'une résidence sans authentification.
- Ajout d'une bannière pour l'importation de logements.
- Ajout d'aides pour les conseillers d'orientation.
- Ajout de la possibilité d'ajouter/supprimer un logement des favoris directement depuis la page de détails.
- Amélioration de la conservation des paramètres de recherche lors du clic sur un résultat de l'autocomplétion.
- Ajout de la possibilité de filtrer les logements par type (ex: CROUS).
- Ajout d'un champ "wifi" aux caractéristiques du logement.
- Ajout d'un bouton d'appel à l'action pour le simulateur de budget.

### Évolutions techniques
- Mise à jour du système d'authentification.
- Refactorisation du code pour améliorer les performances et la stabilité (préchargement et mise en cache).
- Amélioration de la gestion des erreurs et des états de chargement (suspense/squelettes).
- Correction de problèmes liés à l'utilisation de plugins Tiptap.
- Amélioration de la gestion des URL et des redirections.
- Optimisation de la gestion des images (compression, positionnement).
- Mise à jour de la configuration Next.js.
- Suppression de code obsolète (parcoursup results, logs).

### Autres changements
- Amélioration des textes et des libellés (wordings).
- Corrections de bugs d'affichage et de responsivité.
- Amélioration de l'accessibilité.
- Ajout de liens vers les mentions légales et les CGU.
- Amélioration de la documentation et du fichier README.
- Corrections de bugs liés à l'internationalisation (i18n).
- Amélioration de l'UX/UI de divers composants (widget de recherche, formulaire de création de résidence, etc.).
- Corrections de bugs liés à la gestion des couleurs sur les graphiques.
- Ajout de tests et de validations.
