## Changelog : histologe (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interconnexion avec le SI Santé Habitat (SISH), la gestion des signalements et des bailleurs, ainsi que des corrections de bugs et des optimisations techniques. Des améliorations d'accessibilité et de sécurité ont également été apportées.

### Évolutions fonctionnelles
- **Connexion SI Santé Habitat (SISH)** :
    - Envoi de l'adresse complète du bailleur lors de la transmission au SISH [#6135](https://github.com/MTES-MCT/histologe/issues/6135).
    - Optimisation de la page de connexion SI suite aux dernières évolutions [#6138](https://github.com/MTES-MCT/histologe/issues/6138).
    - Possibilité de désactiver les appels à OVH S3 en cas de dysfonctionnement [#6117](https://github.com/MTES-MCT/histologe/issues/6117).
    - Reprise des dossiers SCHS pour le SI Santé Habitat [#6090](https://github.com/MTES-MCT/histologe/issues/6090).
    - Suivi automatique interne ajouté à l'historique de l'adresse lors de l'enregistrement d'un signalement [#6056](https://github.com/MTES-MCT/histologe/issues/6056).
- **Gestion des signalements** :
    - Commande temporaire de clôture de signalements (bis) [#6105](https://github.com/MTES-MCT/histologe/issues/6105) et [#6040](https://github.com/MTES-MCT/histologe/issues/6040).
    - Ajout d'un filtre "Démarche accélérée" dans la liste des signalements [#6041](https://github.com/MTES-MCT/histologe/issues/6041).
    - Possibilité de clôturer des signalements en masse à partir d'un fichier CSV [#6020](https://github.com/MTES-MCT/histologe/issues/6020).
- **Gestion des bailleurs** :
    - Mise en avant des erreurs de données et amélioration de la reprise des dossiers en erreur lors de la connexion avec Esabora [#6110](https://github.com/MTES-MCT/histologe/issues/6110).
    - Copie de l'interface de login standard pour les bailleurs [#6073](https://github.com/MTES-MCT/histologe/issues/6073).
- **Autres** :
    - Améliorations rapides de l'espace bailleur (injonctions) [#6023](https://github.com/MTES-MCT/histologe/issues/6023).
    - Affinement du système de relances pour la démarche accélérée [#6053](https://github.com/MTES-MCT/histologe/issues/6053).
    - Ajout d'un bandeau d'alerte pour les environnements de test [#6081](https://github.com/MTES-MCT/histologe/issues/6081).

### Évolutions techniques
- **Architecture & Performance** :
    - Rationalisation des flush de la base de données (première étape) [#5977](https://github.com/MTES-MCT/histologe/issues/5977).
    - Adaptation de EtageParser pour se caler sur les contraintes d'Esabora [#6106](https://github.com/MTES-MCT/histologe/issues/6106).
- **Sécurité** :
    - Mise à jour de Jmespath suite à une CVE détectée [#6028](https://github.com/MTES-MCT/histologe/issues/6028).
- **API** :
    - Correction de la pagination de l'API [#6075](https://github.com/MTES-MCT/histologe/issues/6075).
- **Socle arrêté** : Mise en place d'un socle pour la gestion des arrêtés [#6014](https://github.com/MTES-MCT/histologe/issues/6014).

### Autres changements
- Amélioration de la navigation au clavier dans le formulaire Pro [#6005](https://github.com/MTES-MCT/histologe/issues/6005).
- Corrections diverses HTML sur la page du dossier bailleur [#6076](https://github.com/MTES-MCT/histologe/issues/6076).
- Amélioration de l'accessibilité du login utilisateur [#6093](https://github.com/MTES-MCT/histologe/issues/6093).
- Suppression du résumé des suivis généré par l'IA [#6039](https://github.com/MTES-MCT/histologe/issues/6039).
- Correction d'une erreur de type lors de la normalisation du code INSEE [#6062](https://github.com/MTES-MCT/histologe/issues/6062).
- Correction d'un crash lors de l'ajout d'un utilisateur à un partenaire sans email activé [#6017](https://github.com/MTES-MCT/histologe/issues/6017).
- Correction d'une erreur d'export de liste [#6062](https://github.com/MTES-MCT/histologe/issues/6062).
- Mise à jour des paquets npm [#6037](https://github.com/MTES-MCT/histologe/issues/6037).
- Correction de l'envoi de mails Brevo (suivi des erreurs) [#5952](https://github.com/MTES-MCT/histologe/issues/5952).
