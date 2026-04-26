## Changelog : rdv-service-public (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des utilisateurs et des espaces, notamment en termes de sécurité (double authentification), de création d'espaces via les OPSN, et d'informations affichées (SIRET, nombre d'habitants). Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant l'affichage des agendas et des plages horaires.

### Évolutions fonctionnelles
- **Sécurité :** Mise en place de la double authentification (2FA) pour certains comptes sensibles et via ProConnect [#6310, #6335].
- **Gestion des espaces :**
    - Création automatique d'un espace lors de l'activation de rdv-service-public par un OPSN [#6304].
    - Ajout du SIRET sur l'espace [#6302].
    - Correction de la création d’espace via les OPSN [#6336].
- **Gestion des utilisateurs :**
    - Ajout du nombre d’habitants de la commune lors de la demande d’ouverture de compte [#6321].
    - Possibilité de se désinscrire d'une liste d'attente en un clic [#6288].
    - Envoi d'un email en cas de refus de demande d’ouverture de compte [#6278].
    - Correction de l'affichage des usagers ayant le même email [#6286].
- **API :** Ajout des champs de geocoding dans le blueprint users pour l'API V1 [#6337]. Ajout du champ `time_zone` dans l'API `rdvs` [#6340].
- **Interface utilisateur :**
    - Passage des formulaires de création/édition d'agent au Design System Français (DSFR) [#6309].
    - Amélioration de l'affichage de la sélection de date et heure d'une plage [#6292].
    - Rendre le bouton "Retour à l'accueil" contextuel sur l’écran de sélection d’organisation [#6301].
    - Amélioration de l'affichage du nom de l'espace dans le choix de fiche lors de la connexion d'un usager [#6255].

### Évolutions techniques
- **Node.js :** Mise à jour de Node.js en version 24 pour améliorer la sécurité et les performances [#6296, #6299].
- **Tests :** Correction de plusieurs tests "flaky" (tests qui échouent de manière aléatoire) en utilisant `travel_to` de Playwright et en corrigeant des problèmes liés aux jours fériés [#6312, #6290, #6315, #6326].
- **Performance :** Limitation de l'usage mémoire par `FileAttenteJob` en le séparant en plusieurs jobs [#6324]. Rendre `FileAttenteJob` plus robuste [#6322].
- **Code :** Suppression du code de l'ancien calculateur de créneaux [#6295]. Nettoyage du code des connexions supplémentaires à la base de données [#6297]. Suppression du markup Stimulus sur `_recurrence.html.slim` [#6291].
- **Dépendances :** Mise à jour de `rack-session` de 2.1.1 à 2.1.2 [#6317], de `rack` de 3.2.5 à 3.2.6 [#6311], de `addressable` [#6318], et de `brace-expansion` [#6287, #6289].
- **Correction d'erreurs :** Correction de l'affichage des jours fériés pour l'agenda multi-agent [#6325]. Correction des récurrences sur les plages d'ouverture [#6329].

### Autres changements
- Documentation des cas d'erreur pour visioplainte [#6293].
- Correction de l'affichage de la carte sur la page de statistiques [#6294].
- Mise à jour de la librairie `phonelib` pour prendre en compte les numéros de téléphone récents [#6303].
- Suppression de la rétrocompatibilité du champ `notification_email` [#6281].
