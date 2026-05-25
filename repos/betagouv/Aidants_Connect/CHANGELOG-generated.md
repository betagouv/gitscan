## Changelog : Aidants_Connect (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les référents et les aidants.  Des améliorations ont été apportées aux parcours d'ajout et de changement de structure d'un aidant, ainsi qu'à la page de connexion et à la gestion des attestations de formation. Des corrections de bugs et des ajustements d'interface ont également été réalisés.

### Évolutions fonctionnelles
- **Gestion des aidants :** Refonte complète du parcours d'ajout d'un aidant, incluant la possibilité de changer la structure associée à un aidant [#1736].
- **Exports :** Amélioration des exports des inscrits pour les Organismes de Formation (OF) [#1778] et pour la formation des aidants.
- **Téléchargement d'attestations :** Ajout d'un bouton permettant aux référents de télécharger l'attestation de formation des aidants [#1770].
- **Page de connexion :** Ajout d'informations pour les particuliers sur la page de connexion et amélioration de la mise en page et des icônes [#1769].
- **Navigation :** Simplification du menu de l'espace aidant et restructuration des URLs [#1751].
- **Affichage des résultats :** Ajout du nombre de résultats trouvés dans le titre des onglets de recherche [#1771].
- **Correction d'URL :** Correction d'une erreur d'URL de callback [#1776].
- **Formulaire de changement de structure :** Amélioration de la validation de l'email et ajout de tests pour le formulaire de changement de structure.

### Évolutions techniques
- **Refactoring URLs :** Refactorisation des URLs dans les templates et les tests pour utiliser les nouveaux espaces de noms.
- **Espaces de noms URL :** Création d'espaces de noms URL pour l'espace aidant et le référent.
- **Tests :** Ajout de tests pour la validation de l'email lors d'une demande de changement de structure déjà en cours.
- **Amélioration du code HTML :** Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- **DSFR :** Correction d'un problème d'alignement dans le DSFR en ajustant les propriétés flex pour les éléments fieldset.

### Autres changements
- **Budget 2025 :** Ajout du budget 2025 [#1768].
- **Correction FAQ URL:** Correction d'une URL de la FAQ [#1778].
- **Amélioration des messages :** Petites modifications de formulation dans le parcours de changement de structure [#1774].
