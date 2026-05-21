## Changelog : Aidants_Connect (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, Aidants Connect a bénéficié d'une refonte significative du parcours de changement de structure pour les aidants, ainsi que d'améliorations de l'interface utilisateur et de corrections de bugs. Des fonctionnalités ont été ajoutées pour faciliter le téléchargement des attestations de formation et l'accès aux informations pour les particuliers. L'expérience utilisateur a été améliorée grâce à une simplification du menu et à l'ajout d'informations contextuelles.

### Évolutions fonctionnelles
- **Changement de structure :** Refonte complète du parcours de changement de structure pour les aidants, incluant des améliorations de la validation des emails et des messages d'erreur. [#1736](https://github.com/betagouv/Aidants_Connect/issues/1736)
- **Téléchargement d'attestation :** Ajout d'un bouton permettant aux référents de télécharger l'attestation de formation des aidants qu'ils gèrent. [#1770](https://github.com/betagouv/Aidants_Connect/issues/1770)
- **Page de connexion :** Amélioration de la page de connexion avec des informations supplémentaires pour les particuliers et une mise à jour du design. [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769)
- **Nombre de résultats :** Affichage du nombre de résultats trouvés dans le titre des onglets de recherche. [#1771](https://github.com/betagouv/Aidants_Connect/issues/1771)
- **Message d'erreur de connexion :** Affichage d'un message d'erreur générique en cas d'échec de connexion. [#1772](https://github.com/betagouv/Aidants_Connect/issues/1772)
- **Menu de l'espace aidant :** Simplification du menu de l'espace aidant et restructuration des URL. [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751)
- **Budget 2025 :** Ajout du budget 2025. [#1768](https://github.com/betagouv/Aidants_Connect/issues/1768)

### Évolutions techniques
- **Refactoring URL :** Refactorisation des URLs dans les templates et les tests pour utiliser les nouveaux espaces de noms.
- **Espaces de noms URL :** Création d'espaces de noms URL pour l'espace aidant et le référent.
- **Tests :** Ajout de `wait until` pour éviter les tests instables.
- **Amélioration du template aidant.html :** Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- **Correction URL de callback :** Correction d'une erreur d'URL de callback. [#1776](https://github.com/betagouv/Aidants_Connect/issues/1776)

### Autres changements
- Correction de l'URL de la FAQ.
- Petites modifications de formulation dans le parcours de changement de structure. [#1774](https://github.com/betagouv/Aidants_Connect/issues/1774)
- Mise à jour du message de confirmation.
- Correction d'un problème d'alignement dans le DSFR en ajustant les propriétés flex pour les éléments fieldset.
