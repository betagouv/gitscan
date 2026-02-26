## Changelog : plusfraichemaville-site (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées au site Plus Fraîche Ma Ville au cours du dernier mois. Les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des estimations et des projets, ainsi que sur des corrections de bugs et des optimisations techniques. La gestion des collectivités et l'intégration avec l'API adresse ont également été améliorées.

### Évolutions fonctionnelles
- Possibilité de voir tous les projets pour une EPCI ou une commune (#469).
- Amélioration de l'affichage des aides et financements : suppression de l'affichage des aides régionales et du lien vers les fonds verts (#471).
- Ajout d'un avertissement de prix pour les territoires ultramarins (#470).
- Amélioration de la gestion des fiches solutions dans les estimations :
    - Possibilité d'ajouter des fiches solutions à une estimation (#467).
    - Possibilité de supprimer une fiche solution d'une estimation (#465).
    - Tri des fiches solutions dans l'estimation (#467).
    - Correction de l'ouverture de la modale de création d'estimation (#465).
- Affichage de Climadiag pour la commune ou l'EPCI de l'utilisateur (#464).
- Amélioration de la gestion des collectivités : ajout d'une alerte Mattermost lorsqu'un utilisateur n'a pas de SIREN (#465).
- Changement de l'API adresse utilisée (#464).
- Modification de l'ordre des boutons dans la modale d'estimation (#462).
- Correction de l'index de la fiche solution dans l'ouverture de la modale d'estimation (#472).
- Correction du z-index des options de maturité sur la carte projet (#460).
- Correction d'un crash lors de la navigation entre différents projets avec une estimation en cours (#461).

### Évolutions techniques
- Mise à jour de Next.js et jsPDF pour corriger des failles de sécurité (#463).
- Suppression du code HubSpot non utilisé (#472).
- Refactoring du code pour améliorer la lisibilité et la maintenabilité (plusieurs commits).
- Correction de warnings TypeScript (#468).
- Création d'un script pour peupler les nouvelles tables EPCI et commune (#468).
- Suppression de l'utilisation de `UserWithCollectivite` lorsque ce n'est pas nécessaire (#464).
- Suppression de la liaison entre Collectivité et Utilisateur (en cours de développement) (#464).

### Autres changements
- Nettoyage de code et ajustements de style (plusieurs commits).
- Ajustement de la marge pour correspondre au design (#466).
- Ajout d'une icône au premier label du fil d'Ariane.
