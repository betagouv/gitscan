## Changelog : Aidants_Connect (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans les parcours de gestion des aidants et des structures. Des corrections ont été apportées pour améliorer la robustesse de l'application et la clarté des messages affichés. De nouvelles fonctionnalités ont été ajoutées pour faciliter le téléchargement d'attestations de formation et l'accès à des informations pour les particuliers.

### Évolutions fonctionnelles
- Amélioration du parcours d'ajout d'aidant, incluant la gestion du changement de structure [#1736](https://github.com/betagouv/Aidants_Connect/issues/1736).
- Simplification du menu de l'espace aidant et restructuration des URLs [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751).
- Ajout d'informations pour les particuliers sur la page de connexion [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769).
- Ajout d'un bouton pour les référents permettant de télécharger l'attestation de formation des aidants [#1770](https://github.com/betagouv/Aidants_Connect/issues/1770).
- Affichage du nombre de résultats trouvés dans le titre des onglets [#1771](https://github.com/betagouv/Aidants_Connect/issues/1771).
- Affichage d'un message d'erreur générique en cas d'échec de connexion [#1772](https://github.com/betagouv/Aidants_Connect/issues/1772).
- Correction de l'URL de callback FranceConnect [#1776](https://github.com/betagouv/Aidants_Connect/issues/1776).
- Ajout du budget 2025 [#1768](https://github.com/betagouv/Aidants_Connect/issues/1768).
- Correction d'une faute de frappe dans l'attestation [#1767](https://github.com/betagouv/Aidants_Connect/issues/1767).

### Évolutions techniques
- Refactoring des URLs dans les templates et les tests pour utiliser les nouveaux espaces de noms.
- Utilisation de `reverse()` et d'espaces de noms dans les tests.
- Création d'espaces de noms d'URL pour l'espace aidant et le référent.
- Amélioration de la validation de l'adresse e-mail dans le formulaire de demande de changement de structure, avec ajout de tests.
- Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- Ajout de tests avec `wait until` pour éviter les tests instables.

### Autres changements
- Petites modifications de formulation dans le parcours de changement de structure [#1774](https://github.com/betagouv/Aidants_Connect/issues/1774).
- Mise à jour du message de confirmation.
- Correction de l'alignement d'éléments dans le DSFR en ajustant les propriétés flexbox.
- Correction de la taille des icônes sur les petits écrans.
- Suppression de l'ancienne page de connexion et mise à jour des styles de la nouvelle page.
