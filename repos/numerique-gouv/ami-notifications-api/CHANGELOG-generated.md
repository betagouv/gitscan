## Changelog : ami-notifications-api (30 derniers jours, au 05 juin 2026)

### Résumé
Les dernières mises à jour de l'API ami-notifications-api se concentrent sur l'amélioration de l'expérience utilisateur de l'application mobile interministérielle (AMI), notamment en permettant une gestion plus fine des préférences de localisation et des notifications. Des travaux importants ont également été réalisés sur l'administration des utilisateurs et la réplication de la base de données. Enfin, des améliorations techniques ont été apportées pour la sécurité et la maintenance du code.

### Évolutions fonctionnelles
- **Gestion des préférences de localisation :** Amélioration significative de la gestion des zones et des adresses dans l'application mobile :
    - Possibilité de supprimer une adresse depuis les préférences (#789).
    - Ajout de la recherche de villes au format BAN (#789).
    - Sélection de zone par ville (#789).
    - Affichage et gestion des zones de vacances (#802).
    - Navigation vers les préférences de zone lors de la première connexion (#788).
- **Notifications :**
    - Mise à jour du lien des notifications pour rediriger vers la page de suivi correspondante (#794).
    - Désactivation des notifications lors de la déconnexion (#721).
- **Administration des utilisateurs :**
    - Ajout de vues et d'une logique pour la recherche, la consultation et la suppression d'utilisateurs dans l'interface d'administration (#774).
    - Ajout d'entrées d'audit pour les actions de consultation et de suppression d'utilisateurs (#774).
- **Notifications planifiées :**
    - Ajout du champ `content_private_body` aux modèles de notification et de suivi pour permettre le stockage d'informations sensibles (#875).
    - Amélioration de l'interface pour la gestion des notifications planifiées, notamment la gestion de la date (#852).
- **FranceConnect et FISession :** Implémentation d'un nouveau flux d'authentification avec FranceConnect et gestion des sessions FISession (#708).

### Évolutions techniques
- **Réplication de la base de données :** Mise en place d'un mécanisme de réplication de la base de données vers un datawarehouse (#904, #791).
- **Sécurité :**
    - Utilisation de `mkcert` pour la gestion des certificats SSL locaux (#828).
    - Suppression du `target="_self"` dans le code Svelte pour améliorer la sécurité (#877).
- **Infrastructure :**
    - Chargement de la variable d'environnement `DEBUG` à partir du fichier `.env.local` (#905).
    - Amélioration de la gestion des certificats SSL pour les environnements locaux.
- **Refactoring et maintenance :**
    - Suppression de code obsolète et de fonctionnalités inutilisées (#823).
    - Amélioration de la structure du code et de la lisibilité.
    - Mise à jour de plusieurs dépendances (uv, twisted, urllib3, svelte, vitest, idna, ujson, @sveltejs/kit, ws).
    - Suppression d'un champ inutile dans le modèle `ScheduledNotification` (#914).

### Autres changements
- Amélioration des messages de confirmation (toasts) et des bannières (#723).
- Ajout de tests et correction de bugs mineurs.
- Mise à jour de la documentation.
- Amélioration du logging.
- Ajout de suivi Matomo pour les zones de vacances (#750).
- Amélioration de la mise en page du bouton "gérer" dans l'écran des notifications (#874).
- Ajout d'un composant `PageWrapper` pour une mise en page cohérente (#801).
