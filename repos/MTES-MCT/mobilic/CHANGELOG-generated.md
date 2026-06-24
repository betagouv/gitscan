## Changelog : mobilic (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment au niveau de la gestion des missions et de l'affichage des informations pour les administrateurs. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier sur le tableau de bord administrateur. L'interface utilisateur a été améliorée avec l'utilisation de composants DSFR et une meilleure gestion de l'affichage des données.

### Évolutions fonctionnelles
- Amélioration de l'affichage des activités pour les employés : le format de l'heure a été modifié pour plus de clarté. [#880](https://github.com/MTES-MCT/mobilic/pull/880)
- Modification du bouton "Edition" d'activité pour utiliser un composant DSFR, améliorant l'harmonie visuelle. [#879](https://github.com/MTES-MCT/mobilic/pull/879)
- Modification du bouton "Remplacer" une activité. [#870](https://github.com/MTES-MCT/mobilic/pull/870)
- Masquage du champ "Conducteur" pour les utilisateurs non-équipe dans la révision d'activité. [#875](https://github.com/MTES-MCT/mobilic/pull/875)
- Rafraîchissement des données après validation d'une mission dans le panneau de validation administrateur. [#873](https://github.com/MTES-MCT/mobilic/pull/873)
- Correction permettant de sélectionner "Accompagnement" dans le menu déroulant lors de la révision d'une activité. [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- Correction pour utiliser le paramètre d'accompagnement pour afficher l'étiquette "Conduite". [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- Ajout d'une étiquette d'alerte de travail de nuit dans le panneau de respect de la réglementation (admin). [#843](https://github.com/MTES-MCT/mobilic/pull/843)
- Ajout d'une recherche pour les NATINF. [#861](https://github.com/MTES-MCT/mobilic/pull/861) et [#860](https://github.com/MTES-MCT/mobilic/pull/860) et [#853](https://github.com/MTES-MCT/mobilic/pull/853)
- Renommage du bouton "Conduire" en "Travail" lorsque les autres tâches sont désactivées. [#855](https://github.com/MTES-MCT/mobilic/pull/855) et [#867](https://github.com/MTES-MCT/mobilic/pull/867) et [#864](https://github.com/MTES-MCT/mobilic/pull/864)
- Amélioration de la documentation du contrôleur et des liens vers les vidéos. [#854](https://github.com/MTES-MCT/mobilic/pull/854) et [#861](https://github.com/MTES-MCT/mobilic/pull/861)

### Évolutions techniques
- Optimisation des requêtes du tableau de bord administrateur pour améliorer les performances. [#865](https://github.com/MTES-MCT/mobilic/pull/865)
- Refactorisation du code pour supprimer le filtrage hebdomadaire côté client sur la page d'accueil. [#856](https://github.com/MTES-MCT/mobilic/pull/856)
- Correction d'un problème de téléchargement de l'historique du contrôleur C1B. [#857](https://github.com/MTES-MCT/mobilic/pull/857)
- Correction d'un problème d'agrégation du tableau des temps de travail dans les vues hebdomadaires et mensuelles. [#844](https://github.com/MTES-MCT/mobilic/pull/844)
- Correction d'un bug lié au rafraîchissement des jours de travail après la validation d'une mission. [#854](https://github.com/MTES-MCT/mobilic/pull/854)
- Correction d'une typographie dans la documentation. [#871](https://github.com/MTES-MCT/mobilic/pull/871)
- Correction d'un problème avec le bouton de soumission fixe sur le résumé de la mission. [#868](https://github.com/MTES-MCT/mobilic/pull/868)
- Correction de l'affichage des infractions dans l'interface du contrôleur.
- Correction de l'affichage des infractions dans l'interface du contrôleur.

### Autres changements
- Amélioration de la documentation et des liens vers les ressources du contrôleur.
- Correction de quelques wordings sur la page d'accueil administrateur. [#851](https://github.com/MTES-MCT/mobilic/pull/851) et [#858](https://github.com/MTES-MCT/mobilic/pull/858)
- Correction de l'affichage des infractions sur la page d'accueil administrateur.
- Correction du format de date pour l'export C1B.
- Amélioration du style et de l'organisation des composants d'alerte du contrôleur.
- Correction de l'affichage des infractions dans l'interface du contrôleur.
