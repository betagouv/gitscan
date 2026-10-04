## Changelog : zacharie (30 derniers jours, au 1er octobre 2026)

### Résumé
Ce mois-ci, Zacharie a franchi une étape importante dans l'amélioration de l'expérience des fédérations avec une refonte de leurs tableaux de bord et un accès élargi aux données départementales. Le suivi de la traçabilité a été fluidifié, notamment pour les circuits courts et les processus de vente/don. Parallèlement, une attention majeure a été portée à la sécurité des données personnelles et à la performance de l'application, qui est désormais deux fois plus légère au chargement.

### Évolutions fonctionnelles
- **Tableaux de bord et statistiques** : Refonte visuelle du tableau de bord des fédérations selon les nouvelles maquettes [#641] et possibilité pour les fédérations nationales et régionales d'accéder aux tableaux de bord départementaux [#696]. Les statistiques Metabase sont également mises à jour pour le nouveau modèle de fiche [#679].
- **Traçabilité et flux de travail** : 
    - Amélioration du circuit court : l'expéditeur reçoit désormais une copie de la fiche et est alerté si le destinataire ne l'a pas reçue [#695].
    - Optimisation de la gestion des retours : correction des flux de carcasses renvoyées pour éviter les doublons ou les erreurs d'attribution [#688, #691, #654].
    - Ajout de nouveaux champs utiles : possibilité d'ajouter un numéro de bon de réception [#577] et des commentaires optionnels sur les carcasses [#607].
- **Vente et Don** : Simplification de l'interface de vente/don pour plus de clarté [#619, #620] et possibilité pour les chasseurs d'ajouter directement des collecteurs professionnels comme destinataires [#659].
- **Administration** : 
    - Création simplifiée de destinataires (commerces, cantines, associations, etc.) directement depuis l'interface d'administration [#652].
    - Nouveaux outils de gestion des utilisateurs : affichage du nombre de carcasses/fiches par utilisateur et gestion des blocages de compte (déblocage, réinitialisation) [#663, #640].
- **Export et données** : L'export Excel des fiches inclut désormais le nombre d'animaux acceptés pour le petit gibier [#683].

### Évolutions techniques
- **Sécurité et protection des données** : 
    - Renforcement de la confidentialité : les mots de passe, jetons de session et données personnelles ne sont plus transmis aux outils de suivi (Sentry) ou dans les logs [#682].
    - Sécurisation des échanges : correction de failles de redirection malveillante [#678], protection des clés privées lors de la modification des accords de partage [#675] et limitation des tentatives de connexion pour prévenir les attaques par force brute [#673].
    - Sécurisation de l'API : obligation d'utiliser un secret de session en production [#671].
- **Performance** : Optimisation majeure ayant permis de diviser par deux le poids de l'application lors du chargement initial [#643].
- **Infrastructure et outils** : 
    - Intégration de ProConnect pour les administrateurs [#605].
    - Amélioration de l'observabilité avec l'ajout de dimensions personnalisées dans Matomo pour suivre les rôles et statuts des utilisateurs [#632].
    - Utilisation de la nouvelle bibliothèque `react-dsfr-chart` pour les graphiques [#650].

### Autres changements
- Mise à jour de la documentation interne et de la configuration de formatage du code (Prettier) [#637].
- Désactivation de ProConnect en environnement de développement pour faciliter les tests [#638].
