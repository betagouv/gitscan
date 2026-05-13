## Changelog : Aidants_Connect (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les aidants et les référents, notamment au niveau des parcours de modification de structure, de la gestion des attestations de formation, et de la page de connexion. Des améliorations de la présentation et de la clarté de l'information ont également été apportées.

### Évolutions fonctionnelles
- **Parcours de changement de structure :** Refonte du parcours d'ajout d'aidant et de changement de structure, avec des améliorations de la formulation et de la validation des informations saisies. [#1736](https://github.com/betagouv/Aidants_Connect/issues/1736)
- **Attestation de formation :** Ajout d'un bouton pour les référents permettant de télécharger l'attestation de formation des aidants. [#1770](https://github.com/betagouv/Aidants_Connect/issues/1770)
- **Page de connexion :** Amélioration de la mise en page et ajout de nouvelles icônes sur la page de connexion, avec un message d'erreur générique en cas d'échec. [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769), [#1772](https://github.com/betagouv/Aidants_Connect/issues/1772)
- **Informations pour les particuliers :** Ajout d'informations dédiées aux particuliers sur la page de connexion. [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769)
- **Nombre de résultats :** Affichage du nombre de résultats trouvés dans le titre des onglets de recherche. [#1771](https://github.com/betagouv/Aidants_Connect/issues/1771)
- **Mandats :** Ajout de cadres pour les signatures dans les mandats. [#1750](https://github.com/betagouv/Aidants_Connect/issues/1750)
- **Publication des formations :** Possibilité de ne pas publier les formations. [#1759](https://github.com/betagouv/Aidants_Connect/issues/1759)
- **Correction orthographique :** Correction d'une faute d'orthographe dans l'attestation. [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758)

### Évolutions techniques
- **Refactoring URLs :** Refactorisation des URLs dans les templates et les tests pour utiliser les nouveaux espaces de noms.
- **Espaces de noms URL :** Création d'espaces de noms URL pour l'espace aidant et le référent.
- **Simplification du menu :** Simplification du menu de l'espace aidant et restructuration des URLs. [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751)
- **Mise à jour du template mandat :** Mise à jour du template mandat pour ajuster la taille du logo et améliorer le CSS pour la mise en page et les signatures.
- **Amélioration du code :** Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- **Tests :** Ajout de tests pour la validation du changement d'email et utilisation de `reverse()` et des espaces de noms dans les tests.

### Autres changements
- **Mise à jour du budget :** Ajout du budget 2025. [#1768](https://github.com/betagouv/Aidants_Connect/issues/1768)
- **Clarification de l'audience :** Mise à jour de l'en-tête et du pied de page pour indiquer clairement que Aidants Connect s'adresse aux professionnels. [#1760](https://github.com/betagouv/Aidants_Connect/issues/1760)
- **Correction d'un bug d'alignement :** Correction d'un problème d'alignement dans le DSFR en ajustant les propriétés flex pour les éléments fieldset.
- **Mise à jour des liens de webinaire :** Plusieurs mises à jour des liens d'inscription au webinaire. [#1762](https://github.com/betagouv/Aidants_Connect/issues/1762), [#1763](https://github.com/betagouv/Aidants_Connect/issues/1763), [#1764](https://github.com/betagouv/Aidants_Connect/issues/1764), [#1765](https://github.com/betagouv/Aidants_Connect/issues/1765)
- **Correction d'un typo :** Correction d'un typo dans l'attestation. [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758)
