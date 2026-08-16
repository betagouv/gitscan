## Changelog : tacct-legacy-nextjs (30 derniers jours, au 14/08/2026)

### Résumé
Cette période a été marquée par l'ajout de fonctionnalités clés pour la gestion des utilisateurs (invitations, accès administrateur) et l'optimisation du parcours lié aux études. Des corrections visuelles et fonctionnelles ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : Ajout de la fonctionnalité d'invitation de nouveaux comptes et ouverture de l'accès aux paramètres (settings) pour les profils administrateurs.
- **Gestion des études** : Amélioration du processus de sélection et de persistance lors du changement d'étude, incluant désormais le transfert de la commune lors du transfert d'une étude.
- **Corrections** : 
    - Résolution d'un problème lié aux recettes (salve 2) [#1439](https://github.com/incubateur-ademe/tacct-legacy-nextjs/issues/1439).
    - Correction d'un bug d'affichage de la largeur des champs de saisie sur les anciens navigateurs.

### Évolutions techniques
- **Base de données** : Suppression de la gestion des catastrophes naturelles (*natural disaster*) dans le schéma.
- **Infrastructure et déploiement** : Ajustements de la configuration de l'envoi d'origine (`x-forwarded-host`) et mise à jour de l'adresse e-mail d'administration pour le déploiement.

### Autres changements
- Mise à jour du contenu textuel des e-mails d'invitation.
