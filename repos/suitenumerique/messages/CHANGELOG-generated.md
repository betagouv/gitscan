## Changelog : messages (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau de la navigation dans les threads, de la composition des messages et de la gestion des boîtes de réception. Des améliorations de sécurité et de performance ont également été apportées, ainsi qu'une refonte technique majeure du frontend avec le passage à Vite et TanStack Router.

### Évolutions fonctionnelles
- **Threads :** Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons. [#707](https://github.com/suitenumerique/messages/issues/707)
- **Boîtes de réception :** Amélioration de la navigation et de l'accessibilité des boîtes de réception, ainsi que de l'expérience utilisateur du menu déroulant des boîtes de réception. [#708](https://github.com/suitenumerique/messages/issues/708) [#705](https://github.com/suitenumerique/messages/issues/705)
- **Paramètres des boîtes de réception :** Regroupement des paramètres des boîtes de réception dans une boîte de dialogue dédiée.
- **Comportement des messages :** Gestion améliorée des pièces jointes de type `message/delivery-status` lors de la composition de messages.
- **Calendrier :** Possibilité de lier une instance CalDAV pour accepter directement les événements. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Assignation de threads :** Possibilité d'assigner un thread à un utilisateur. [#645](https://github.com/suitenumerique/messages/issues/645)
- **Prévisualisation des pièces jointes :** Ajout de la prévisualisation des pièces jointes. [#676](https://github.com/suitenumerique/messages/issues/676)
- **Liens profonds vers les threads :** Ajout de liens directs vers des threads spécifiques. [#664](https://github.com/suitenumerique/messages/issues/664)

### Évolutions techniques
- **Frontend :** Refonte complète du frontend avec le passage de Next.js à Vite et TanStack Router. [#675](https://github.com/suitenumerique/messages/issues/675)
- **Bibliothèque JMAP :** Utilisation de la nouvelle bibliothèque `jmap-email` pour l'analyse et la composition des emails. [#700](https://github.com/suitenumerique/messages/issues/700)
- **Stockage des blobs :** Refonte du stockage des blobs et des pièces jointes avec une approche en plusieurs niveaux.
- **Backend :** Amélioration des performances des requêtes et correction de problèmes de N+1.
- **Sécurité :** Renforcement de la sécurité de la connexion SMTP et des configurations de proxy. [#706](https://github.com/suitenumerique/messages/issues/706)
- **Authentification :** Possibilité de créer une boîte de réception sans synchronisation d'identité. [#707](https://github.com/suitenumerique/messages/issues/707)
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26. [#689](https://github.com/suitenumerique/messages/issues/689)

### Autres changements
- **Documentation :** Ajout d'une nouvelle illustration pour la page d'accueil. [#702](https://github.com/suitenumerique/messages/issues/702)
- **Tests :** Ajout de scripts de publication PyPI pour `jmap-email`. [#700](https://github.com/suitenumerique/messages/issues/700)
- **Corrections de bugs :** Diverses corrections de bugs concernant l'importation de boîtes aux lettres, le traitement des événements récurrents du calendrier, et le fonctionnement général de l'application.
- **Nettoyage du code :** Suppression de champs de modèle dépréciés et ajout de la bibliothèque `defusedxml` pour une meilleure sécurité.
