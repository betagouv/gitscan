## Changelog : mobilic (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment sur les interfaces d'administration et de gestion des missions. Des corrections ont été apportées pour améliorer la clarté des informations affichées et la fluidité des actions, en particulier concernant la validation des missions et la gestion des infractions. Des améliorations de performance ont également été réalisées sur le tableau de bord d'administration.

### Évolutions fonctionnelles
- Amélioration de l'interface de validation des missions : un bouton de soumission fixe a été ajouté pour faciliter la validation sur les appareils mobiles [#868](https://github.com/MTES-MCT/mobilic/pulls/868).
- Modification du libellé du bouton "Conduire" en "Travail" lorsque d'autres tâches sont désactivées, pour une meilleure clarté [#867](https://github.com/MTES-MCT/mobilic/pulls/867) et [#855](https://github.com/MTES-MCT/mobilic/pulls/855).
- Ajout d'une recherche pour les NATINF, facilitant l'accès à ces informations [#861](https://github.com/MTES-MCT/mobilic/pulls/861) et [#860](https://github.com/MTES-MCT/mobilic/pulls/860).
- Amélioration de l'affichage des infractions sur l'interface d'administration, avec une meilleure organisation et une présentation plus claire des informations.
- Correction de l'affichage du champ "Conducteur" dans la révision d'activité en dehors du mode équipe [#875](https://github.com/MTES-MCT/mobilic/pulls/875).
- Correction pour permettre la sélection de "Accompagnement" dans le menu déroulant d'activité [#872](https://github.com/MTES-MCT/mobilic/pulls/872).
- Correction pour que les paramètres de l'entreprise soient respectés et ne soient pas toujours par défaut à "true" [#872](https://github.com/MTES-MCT/mobilic/pulls/872).
- Correction de l'affichage du libellé "Conduite" en mode accompagnement [#872](https://github.com/MTES-MCT/mobilic/pulls/872).
- Correction d'une typographie dans la documentation du contrôleur [#871](https://github.com/MTES-MCT/mobilic/pulls/871).
- Ajout d'un indicateur d'alerte pour le travail de nuit dans le panneau de respect de la réglementation.
- Amélioration du rafraîchissement des données après la validation d'une mission dans le panneau de validation de l'administration [#873](https://github.com/MTES-MCT/mobilic/pulls/873).
- Correction d'un bug empêchant le téléchargement de l'historique du contrôleur C1B [#857](https://github.com/MTES-MCT/mobilic/pulls/857).
- Correction d'un problème lié aux longues pauses dans les données NATINF [#843](https://github.com/MTES-MCT/mobilic/pulls/843).
- Correction de l'agrégation des données du tableau de temps de travail dans les vues hebdomadaires et mensuelles [#844](https://github.com/MTES-MCT/mobilic/pulls/844).
- Correction du format de date pour l'export C1B [#853](https://github.com/MTES-MCT/mobilic/pulls/853).

### Évolutions techniques
- Optimisation des requêtes du tableau de bord de l'administration pour améliorer les performances [#865](https://github.com/MTES-MCT/mobilic/pulls/865).
- Refactorisation du code pour améliorer la réutilisation des étiquettes dans le graphique de respect de la réglementation.
- Refactorisation de l'affichage des infractions dans le contrôleur pour une meilleure organisation.
- Suppression du filtrage hebdomadaire sur le client pour le tableau de bord, améliorant ainsi la performance.
- Restriction de la requête du tableau de bord à la semaine actuelle pour améliorer la performance.

### Autres changements
- Mise à jour de la documentation du contrôleur avec des liens vers les ressources et les vidéos correspondantes [#853](https://github.com/MTES-MCT/mobilic/pulls/853) et [#861](https://github.com/MTES-MCT/mobilic/pulls/861).
- Amélioration de la documentation de la page du contrôleur.
- Corrections de la formulation sur la page d'accueil de l'administration [#851](https://github.com/MTES-MCT/mobilic/pulls/851), [#856](https://github.com/MTES-MCT/mobilic/pulls/856) et [#858](https://github.com/MTES-MCT/mobilic/pulls/858).
