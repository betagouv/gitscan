## Changelog : mobilic (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans l'interface d'administration et la gestion des infractions NATINF. Des corrections de bugs et des ajustements d'interface ont été apportés pour une meilleure ergonomie et une plus grande clarté des informations. L'ajout de la recherche NATINF est en cours d'intégration avec des améliorations continues.

### Évolutions fonctionnelles
- **Interface d'administration :** Amélioration de la page d'accueil avec des informations plus claires sur les employés inactifs et les infractions. Correction de l'affichage des jours à temps plein et des jours multi-employeurs. [#858](https://github.com/MTES-MCT/mobilic/issues/858), [#856](https://github.com/MTES-MCT/mobilic/issues/856), [#851](https://github.com/MTES-MCT/mobilic/issues/851), [#849](https://github.com/MTES-MCT/mobilic/issues/849), [#836](https://github.com/MTES-MCT/mobilic/issues/836)
- **Gestion des infractions NATINF :** Ajout de la fonctionnalité de recherche NATINF, avec des améliorations de l'UX pour l'édition des infractions et l'affichage des résultats. Possibilité de supprimer les infractions NATINF avec une confirmation. [#861](https://github.com/MTES-MCT/mobilic/issues/861), [#860](https://github.com/MTES-MCT/mobilic/issues/860), [#854](https://github.com/MTES-MCT/mobilic/issues/854), [#853](https://github.com/MTES-MCT/mobilic/issues/853)
- **Modalité véhicule :** Suppression des exemples de valeurs dans le formulaire de véhicule dans l'interface d'administration. [#849](https://github.com/MTES-MCT/mobilic/issues/849)
- **Page sécurité :** Mise à jour du texte sur la page de sécurité. [#850](https://github.com/MTES-MCT/mobilic/issues/850)
- **Logo partenaire :** Ajout du logo Chaventon Express. [#848](https://github.com/MTES-MCT/mobilic/issues/848)

### Évolutions techniques
- **Refactoring :** Réorganisation de l'affichage des infractions et du style du texte dans les composants d'alerte. Réorganisation de la section des infractions dans `UserReadAlerts`.  Uniformisation du style du nombre d'alertes et calcul dynamique du temps de la dernière mise à jour des infractions.
- **Composants :** Extraction du composant partagé `AccordionActions` pour corriger les duplications identifiées par SonarCloud.
- **Icônes :** Remplacement des icônes MUI par des icônes DSFR dans les composants d'infraction.
- **Correction de bugs :** Correction de problèmes liés au rafraîchissement des jours de travail après la validation d'une mission. Correction de l'affichage des badges d'alerte et de la direction des icônes fléchées. Correction de l'utilisation de `parseInt` et remplacement par `Number.parseInt`.
- **Améliorations diverses :** Correction de logs d'erreur, ajustement de la hauteur maximale des listes, remplacement des badges inline par des `WarningBadge` dans les composants d'alerte et NATINF.

### Autres changements
- Mise à jour de la documentation et des textes pour améliorer la clarté et la cohérence.
- Correction de noms de classes DSFR invalides.
- Nettoyage de code et suppression de variables et imports inutilisés.
