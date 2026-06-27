## Changelog : mobilic (30 derniers jours, au 25 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur, notamment pour les administrateurs, avec une refonte de la vue des missions et des tableaux de bord. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier au niveau de l'affichage des données et de la gestion des alertes. L'application continue d'évoluer pour offrir une meilleure expérience utilisateur et une plus grande efficacité.

### Évolutions fonctionnelles
- **Vue administrateur des missions :** Amélioration de la structure et de l'ergonomie de la vue des missions pour les administrateurs, incluant des modifications de l'affichage des tags et des en-têtes. [#878](https://github.com/MTES-MCT/mobilic/pull/878)
- **Modification du format de l'heure :** Changement du format d'affichage de l'heure pour les activités, améliorant la lisibilité pour les employés. [#880](https://github.com/MTES-MCT/mobilic/pull/880)
- **Bouton d'édition d'activité :** Utilisation d'un composant DSFR pour le bouton d'édition d'activité, améliorant l'accessibilité et l'apparence. [#879](https://github.com/MTES-MCT/mobilic/pull/879)
- **Bouton "Remplacer activité" :** Refonte du bouton de remplacement d'activité pour une meilleure clarté et une meilleure expérience utilisateur. [#870](https://github.com/MTES-MCT/mobilic/pull/870)
- **Masquage de la sélection du conducteur :** Le champ "Conducteur" est maintenant masqué pour les utilisateurs qui ne sont pas en mode équipe. [#875](https://github.com/MTES-MCT/mobilic/pull/875)
- **Rafraîchissement du panneau de validation :** Correction d'un bug qui empêchait le rafraîchissement des données après la validation d'une mission par un administrateur. [#873](https://github.com/MTES-MCT/mobilic/pull/873)
- **Bouton "Travail" :** Corrections de bugs et améliorations de l'interface du bouton "Travail" dans la vue PWA. [#872](https://github.com/MTES-MCT/mobilic/pull/872)
- **Bouton "Conduire" :** Renommage du bouton "Conduire" lorsque d'autres tâches sont désactivées, pour une meilleure clarté. [#867](https://github.com/MTES-MCT/mobilic/pull/867) et [#855](https://github.com/MTES-MCT/mobilic/pull/855)
- **Recherche NatInf :** Ajout de la fonctionnalité de recherche NatInf. [#861](https://github.com/MTES-MCT/mobilic/pull/861) et [#860](https://github.com/MTES-MCT/mobilic/pull/860) et [#853](https://github.com/MTES-MCT/mobilic/pull/853)
- **Bouton de soumission fixe :** Ajout d'un bouton de soumission fixe en bas de la page de résumé de la mission. [#868](https://github.com/MTES-MCT/mobilic/pull/868)
- **Alertes réglementaires :** Ajout d'une étiquette pour les alertes de travail de nuit dans le panneau de respect de la réglementation. [#844](https://github.com/MTES-MCT/mobilic/pull/844)

### Évolutions techniques
- **Optimisation des performances :** Amélioration des performances de l'application, notamment au niveau des requêtes du tableau de bord administrateur. [#865](https://github.com/MTES-MCT/mobilic/pull/865)
- **Refactorisation du code :** Refactorisation de plusieurs composants pour améliorer la lisibilité et la maintenabilité du code.
- **Documentation :** Amélioration de la documentation du contrôleur et des ressources disponibles. [#863](https://github.com/MTES-MCT/mobilic/pull/863) et [#857](https://github.com/MTES-MCT/mobilic/pull/857) et [#858](https://github.com/MTES-MCT/mobilic/pull/858) et [#856](https://github.com/MTES-MCT/mobilic/pull/856)
- **Correction de bugs :** Correction de plusieurs bugs, notamment liés à l'affichage des données, à la gestion des alertes et à l'exportation des données C1B. [#843](https://github.com/MTES-MCT/mobilic/pull/843)

### Autres changements
- **Amélioration de l'accessibilité :** Ajout de labels pour les icônes afin d'améliorer l'accessibilité.
- **Mise à jour des liens de la documentation :** Mise à jour des liens vers les ressources de documentation du contrôleur.
- **Corrections de typographie :** Correction de plusieurs erreurs de typographie dans la documentation et l'interface utilisateur.
- **Nettoyage du code :** Suppression de variables et d'imports inutilisés.
- **Amélioration du style :** Ajustement du style de certains composants pour une meilleure cohérence visuelle.
