## Changelog : mobilic (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur pour les administrateurs et les employés, notamment dans la gestion des missions et des activités. Des optimisations de performance ont également été apportées, en particulier au niveau du tableau de bord administrateur, et des corrections de bugs ont été implémentées pour améliorer la stabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de la vue des activités pour les administrateurs, avec des corrections de disposition et de tri [#885](https://github.com/MTES-MCT/mobilic/issues/885).
- Modification de l'étiquette pour le transport lourd dans les congés [#887](https://github.com/MTES-MCT/mobilic/issues/887).
- Modification du bouton de remplacement d'activité pour les administrateurs [#870](https://github.com/MTES-MCT/mobilic/issues/870).
- Changement du type de bouton "Modifier activité" pour les employés, utilisation d'un composant DSFR [#879](https://github.com/MTES-MCT/mobilic/issues/879).
- Modification du format de l'heure pour chaque ligne d'activité dans la vue employé [#880](https://github.com/MTES-MCT/mobilic/issues/880).
- Ajout d'un bouton de soumission fixe en bas du résumé de mission [#868](https://github.com/MTES-MCT/mobilic/issues/868).
- Renommage du bouton "Conduire" lorsque d'autres tâches sont désactivées [#867](https://github.com/MTES-MCT/mobilic/issues/867).
- Masquage de la sélection du conducteur pour les missions d'accompagnement [#875](https://github.com/MTES-MCT/mobilic/issues/875).
- Correction de l'affichage du champ "Conducteur" en dehors du mode équipe [#872](https://github.com/MTES-MCT/mobilic/issues/872).
- Correction de l'autorisation de sélectionner "Accompagnement" dans le menu déroulant [#872](https://github.com/MTES-MCT/mobilic/issues/872).

### Évolutions techniques
- Déduplication des requêtes d'historique concurrentes pour la même mission afin d'améliorer les performances [#886](https://github.com/MTES-MCT/mobilic/issues/886).
- Optimisation des performances du tableau de bord administrateur en limitant les requêtes aux données de la semaine en cours [#865](https://github.com/MTES-MCT/mobilic/issues/865).
- Refactorisation du filtrage hebdomadaire sur le client pour simplifier le code [#865](https://github.com/MTES-MCT/mobilic/issues/865).
- Correction d'un problème de rafraîchissement du panneau de validation administrateur [#873](https://github.com/MTES-MCT/mobilic/issues/873).
- Correction d'un bug lié à la configuration de l'entreprise dans la PWA [#872](https://github.com/MTES-MCT/mobilic/issues/872).
- Correction d'une faute de frappe dans la documentation du contrôleur [#871](https://github.com/MTES-MCT/mobilic/issues/871).
- Correction de problèmes liés au téléchargement de l'historique du contrôleur C1B [#857](https://github.com/MTES-MCT/mobilic/issues/857).
- Correction d'un problème d'agrégation des temps de travail dans les vues hebdomadaires et mensuelles [#844](https://github.com/MTES-MCT/mobilic/issues/844).
- Correction d'un problème de longue pause (NATINF_32083) [#843](https://github.com/MTES-MCT/mobilic/issues/843).

### Autres changements
- Amélioration de la documentation de la page du contrôleur [#863](https://github.com/MTES-MCT/mobilic/issues/863).
- Ajout de labels pour améliorer l'accessibilité des icônes [#870](https://github.com/MTES-MCT/mobilic/issues/870).
- Nettoyage du code et des imports [#870](https://github.com/MTES-MCT/mobilic/issues/870).
