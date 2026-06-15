## Changelog : mobilic (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions de mobilic se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les sections de gestion des contrôles et des infractions. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier sur le tableau de bord administrateur. De nouvelles fonctionnalités de recherche et d'affichage ont été implémentées pour faciliter l'utilisation quotidienne de l'application.

### Évolutions fonctionnelles
- Ajout d'une recherche pour les NATINF [#861](https://github.com/MTES-MCT/mobilic/issues/861) et [#860](https://github.com/MTES-MCT/mobilic/issues/860).
- Amélioration de l'UX pour l'édition des infractions dans la section "Alertes" [#850](https://github.com/MTES-MCT/mobilic/issues/850).
- Ajout du logo Chaventon Express [#848](https://github.com/MTES-MCT/mobilic/issues/848).
- Refonte de l'affichage des infractions et amélioration de la gestion des alertes [#860](https://github.com/MTES-MCT/mobilic/issues/860).
- Modification du bouton "Déplacer" en "Travail" lorsqu'une autre tâche est désactivée [#853](https://github.com/MTES-MCT/mobilic/issues/853) et [#864](https://github.com/MTES-MCT/mobilic/issues/864).
- Correction du rafraîchissement des jours de travail après la validation d'une mission [#854](https://github.com/MTES-MCT/mobilic/issues/854).
- Amélioration de l'affichage des infractions liées au travail de nuit sur le tableau de bord administrateur [#855](https://github.com/MTES-MCT/mobilic/issues/855).
- Correction du format de date pour l'export C1B [#853](https://github.com/MTES-MCT/mobilic/issues/853).
- Correction de l'affichage des jours d'activité multiples sur la page d'accueil administrateur [#851](https://github.com/MTES-MCT/mobilic/issues/851).
- Correction de l'affichage des semaines vides et des jours respectant la réglementation sur la page d'accueil administrateur [#851](https://github.com/MTES-MCT/mobilic/issues/851).
- Correction de l'affichage des libellés d'activité de voyage en mode accompagnement [#65fe49c7](https://github.com/MTES-MCT/mobilic/commit/65fe49c7).
- Correction d'un bug empêchant le téléchargement de l'historique du contrôleur C1B [#857](https://github.com/MTES-MCT/mobilic/issues/857).
- Correction d'un problème lié aux pauses longues [#843](https://github.com/MTES-MCT/mobilic/issues/843).
- Correction d'un problème d'agrégation des données du tableau de bord des temps de travail pour les vues hebdomadaires et mensuelles [#844](https://github.com/MTES-MCT/mobilic/issues/844).
- Correction du texte d'aide pour la sélection des infractions [#861](https://github.com/MTES-MCT/mobilic/issues/861).
- Suppression des exemples de valeurs dans le modal des véhicules (admin) [#849](https://github.com/MTES-MCT/mobilic/issues/849).
- Mise à jour du texte de la page de sécurité [#850](https://github.com/MTES-MCT/mobilic/issues/850).

### Évolutions techniques
- Optimisation des requêtes du tableau de bord de la page d'accueil administrateur pour améliorer les performances [#865](https://github.com/MTES-MCT/mobilic/issues/865).
- Refactorisation du code pour supprimer les filtres hebdomadaires sur le client et les restreindre au serveur [#865](https://github.com/MTES-MCT/mobilic/issues/865).
- Utilisation des icônes DSFR au lieu des icônes MUI dans les composants d'infraction [#8691c743](https://github.com/MTES-MCT/mobilic/commit/8691c743).
- Extraction du composant `AccordionActions` partagé pour corriger les duplications identifiées par SonarCloud [#860](https://github.com/MTES-MCT/mobilic/issues/860).
- Amélioration de la documentation de l'API et des contrôleurs [#861](https://github.com/MTES-MCT/mobilic/issues/861).
- Refactorisation de la logique d'affichage des infractions pour une meilleure organisation et lisibilité.

### Autres changements
- Amélioration de la documentation de la page des contrôleurs [#863](https://github.com/MTES-MCT/mobilic/issues/863).
- Correction de liens dans la documentation des ressources du contrôleur [#861](https://github.com/MTES-MCT/mobilic/issues/861).
- Nettoyage du code et suppression de variables inutilisées.
- Correction de logs erronés dans l'administration.
