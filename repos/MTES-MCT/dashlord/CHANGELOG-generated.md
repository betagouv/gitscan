## Changelog : dashlord (30 derniers jours, au 16 juin 2026)

### Résumé
Ce changelog couvre une période d'un mois marquée principalement par des mises à jour automatiques des URLs des sites web surveillés par Dashlord.  Ces mises à jour garantissent que le tableau de bord continue de fonctionner correctement avec les dernières adresses des services de la fabrique numérique. De plus, quelques ajustements de configuration ont été effectués, notamment la suppression d'une entrée obsolète et la modification de l'URL de certains services.

### Évolutions fonctionnelles
- Mise à jour des URLs de nombreux sites web surveillés par Dashlord pour assurer leur bon fonctionnement et la pertinence des données affichées.
- Suppression de l'entrée "a-dock" de la liste des sites surveillés.
- Mise à jour de l'URL de l'application Emile vers `emile.beta.gouv.fr`.

### Évolutions techniques
- Ajustement de la configuration de Dashlord : désactivation des outils de statistiques, de budget, de Dependabot et de Codescan. Désactivation également de Betagouv pour Prelex.
- Mise à jour de l'URL de l'API dans le fichier de configuration `dashlord.yml`.
- Mise à jour des URLs de Trackdechets et Dossier Facile dans le fichier `dashlord.yml`.

### Autres changements
- Intégration des pull requests [#45](https://github.com/MTES-MCT/dashlord/pull/45) pour l'ajout de Prelex et la bascule d'Emile vers l'application.
- Mises à jour régulières du rapport de Dashlord.
