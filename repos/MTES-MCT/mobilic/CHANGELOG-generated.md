## Changelog : mobilic (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface administrateur, avec des optimisations de l'affichage et de la gestion des activités et des missions. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant la gestion des contrôleurs et des alertes. L'accessibilité et la documentation ont également été améliorées.

### Évolutions fonctionnelles
- Amélioration de la vue des activités pour les administrateurs : correction du clic sur les chevrons, mise en page de la colonne des tags et tri des activités validées [#885](https://github.com/MTES-MCT/mobilic/issues/885).
- Modification de l'étiquette pour le transport lourd dans les congés [#887](https://github.com/MTES-MCT/mobilic/issues/887).
- Modification du type de bouton "Modifier l'activité" pour les employés, utilisation d'un composant DSFR [#879](https://github.com/MTES-MCT/mobilic/issues/879).
- Changement du texte du bouton pour améliorer la clarté [#870](https://github.com/MTES-MCT/mobilic/issues/870).
- Ajout d'un bouton de soumission fixe en bas du résumé de mission pour faciliter la validation [#868](https://github.com/MTES-MCT/mobilic/issues/868).
- Renommage du bouton "Conduire" lorsque d'autres tâches sont désactivées pour plus de clarté [#855](https://github.com/MTES-MCT/mobilic/issues/855) et [#867](https://github.com/MTES-MCT/mobilic/issues/867).
- Amélioration de la documentation du contrôleur avec des liens média mis à jour [#864](https://github.com/MTES-MCT/mobilic/issues/864).
- Ajout de la recherche natinf [#861](https://github.com/MTES-MCT/mobilic/issues/861).
- Correction de l'affichage des infractions dans l'interface du contrôleur [#861](https://github.com/MTES-MCT/mobilic/issues/861).
- Correction de l'affichage des en-têtes de section des infractions dans l'interface du contrôleur.

### Évolutions techniques
- Optimisation des performances du tableau de bord de la page d'accueil administrateur en limitant la requête aux données de la semaine en cours [#865](https://github.com/MTES-MCT/mobilic/issues/865).
- Refactorisation de la logique de filtrage hebdomadaire sur la page d'accueil pour améliorer les performances.
- Correction d'un bug empêchant le rafraîchissement des données après la validation d'une mission dans le panneau de validation administrateur [#872](https://github.com/MTES-MCT/mobilic/issues/872).
- Correction d'un problème lié à la gestion des missions PWA (Progressive Web App) [#878](https://github.com/MTES-MCT/mobilic/issues/878).
- Correction d'un problème lié à l'utilisation de `Math.truc` dans le code, identifié par SonarQube [#880](https://github.com/MTES-MCT/mobilic/issues/880).
- Correction d'un bug empêchant la sélection de "Accompagnement" dans le menu déroulant des activités [#871](https://github.com/MTES-MCT/mobilic/issues/871).
- Correction de la gestion des paramètres de l'entreprise dans les missions PWA [#871](https://github.com/MTES-MCT/mobilic/issues/871).
- Correction de la typographie dans la documentation [#871](https://github.com/MTES-MCT/mobilic/issues/871).

### Autres changements
- Amélioration de l'accessibilité des icônes avec des labels associés.
- Nettoyage du code et suppression de variables inutilisées.
- Correction de fautes de frappe dans les textes.
- Mise à jour des liens vers les médias dans la documentation du contrôleur.
- Correction du texte d'aide pour la sélection des infractions.
- Correction de l'affichage des libellés des activités de voyage pour le mode accompagnement.
- Correction du téléchargement de l'historique du contrôleur C1B [#857](https://github.com/MTES-MCT/mobilic/issues/857).
- Correction d'un problème lié aux longues pauses [#843](https://github.com/MTES-MCT/mobilic/issues/843).
- Correction de l'agrégation des données du tableau de temps de travail dans les vues hebdomadaires et mensuelles [#844](https://github.com/MTES-MCT/mobilic/issues/844).
