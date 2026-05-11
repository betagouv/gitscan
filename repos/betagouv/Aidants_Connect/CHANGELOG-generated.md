## Changelog : Aidants_Connect (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du parcours d'ajout d'aidant, de la page de connexion et de la gestion des attestations de formation. Des corrections et des simplifications ont également été apportées pour une meilleure clarté et fluidité de l'application.

### Évolutions fonctionnelles
- **Ajout d'aidant :** Refonte complète du parcours d'ajout d'aidant, avec la possibilité de changer de structure associée [#1736](https://github.com/betagouv/Aidants_Connect/issues/1736).
- **Page de connexion :** Amélioration de la mise en page et ajout de nouvelles icônes pour une meilleure expérience utilisateur. Ajout d'informations spécifiques pour les particuliers [#1769](https://github.com/betagouv/Aidants_Connect/issues/1769).
- **Attestations de formation :** Ajout d'un bouton permettant aux référents de télécharger l'attestation de formation des aidants [#1770](https://github.com/betagouv/Aidants_Connect/issues/1770).
- **Recherche :** Affichage du nombre de résultats trouvés dans le titre des onglets de recherche [#1771](https://github.com/betagouv/Aidants_Connect/issues/1771).
- **Gestion des formations :** Possibilité de publier ou non les formations [#1759](https://github.com/betagouv/Aidants_Connect/issues/1759).
- **Mandats :** Ajout de cadres pour les signatures dans les mandats [#1750](https://github.com/betagouv/Aidants_Connect/issues/1750).
- **Erreurs de connexion :** Affichage d'un message d'erreur générique en cas d'échec de connexion [#1772](https://github.com/betagouv/Aidants_Connect/issues/1772).
- **Mise à jour de l'en-tête et du pied de page :** Clarification du rôle d'Aidants Connect dans l'accompagnement des professionnels [#1760](https://github.com/betagouv/Aidants_Connect/issues/1760).

### Évolutions techniques
- **Refactoring des URLs :** Refactorisation des URLs dans les templates et les tests pour utiliser des namespaces mis à jour.
- **Simplification du menu :** Simplification du menu de l'espace aidant et restructuration des URLs [#1751](https://github.com/betagouv/Aidants_Connect/issues/1751).
- **Amélioration du code :** Refactorisation du template `aidant.html` pour une meilleure lisibilité et cohérence de la structure HTML.
- **Tests :** Ajout de `wait until` dans les tests pour éviter les tests instables.
- **Mise à jour du template de mandat :** Mise à jour du template de mandat vers la version 20260323 (ajustement de la taille du logo et amélioration du CSS pour la mise en page et les signatures).

### Autres changements
- Correction de fautes d'orthographe dans l'attestation [#1758](https://github.com/betagouv/Aidants_Connect/issues/1758).
- Correction d'une URL de la FAQ.
- Mise à jour des liens d'inscription au webinaire.
- Ajout du budget 2025.
- Amélioration de la validation de l'email lors du changement de structure.
