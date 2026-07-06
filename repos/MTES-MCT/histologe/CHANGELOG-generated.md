## Changelog : histologe (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'accessibilité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment pour la gestion des arrêtés, des signalements et l'espace bailleur. Des optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Espace bailleur :** Améliorations de l'interface et ajout de fonctionnalités pour la messagerie, notamment la modification du champ d'upload de fichiers [#5940](https://github.com/MTES-MCT/histologe/issues/5940).
- **Gestion des arrêtés :** Mise en place d'un socle pour la gestion des arrêtés, incluant la liste des arrêtés [#6026](https://github.com/MTES-MCT/histologe/issues/6026) et l'adaptation du parser EtageParser pour répondre aux contraintes d'esabora [#6100](https://github.com/MTES-MCT/histologe/issues/6100).
- **Signalements :**
    - Ajout d'un suivi automatique interne de l'historique de l'adresse lors de l'enregistrement d'un signalement [#6056](https://github.com/MTES-MCT/histologe/issues/6056).
    - Ajout d'un filtre "Démarche accélérée" dans la liste des signalements [#6041](https://github.com/MTES-MCT/histologe/issues/6041).
    - Possibilité de clôturer des signalements en masse via une commande temporaire [#6040](https://github.com/MTES-MCT/histologe/issues/6040).
    - Ajout d'une commande pour fermer des signalements à partir d'un fichier CSV [#5980](https://github.com/MTES-MCT/histologe/issues/5980).
- **Formulaire Pro :** Amélioration de la navigation au clavier et corrections d'accessibilité [#6005](https://github.com/MTES-MCT/histologe/issues/6005) et [#5979](https://github.com/MTES-MCT/histologe/issues/5979).
- **Suivi Usager :** Améliorations d'accessibilité, notamment la précision des liens, l'harmonisation des boutons et le déplacement de l'encart sur le dossier [#5993](https://github.com/MTES-MCT/histologe/issues/5993), [#5994](https://github.com/MTES-MCT/histologe/issues/5994) et [#5996](https://github.com/MTES-MCT/histologe/issues/5996).
- **Environnements de test :** Ajout d'un bandeau d'alerte [#6081](https://github.com/MTES-MCT/histologe/issues/6081).
- **Login bailleur :** Copie de l'interface de login standard [#6073](https://github.com/MTES-MCT/histologe/issues/6073).
- **Mini Dashboard :** Ajout d'un mini dashboard pour la démarche accélérée [#5942](https://github.com/MTES-MCT/histologe/issues/5942).

### Évolutions techniques
- **Rationalisation des flush :** Première étape pour rationaliser les flush de la base de données [#5977](https://github.com/MTES-MCT/histologe/issues/5977).
- **Nettoyage table signalement :** Nettoyage de la table signalement [#5950](https://github.com/MTES-MCT/histologe/issues/5950).
- **Mise à jour des dépendances :** Mise à jour de Jmespath suite à une CVE détectée [#6028](https://github.com/MTES-MCT/histologe/issues/6028) et de npm packages [#5964](https://github.com/MTES-MCT/histologe/issues/5964).
- **Sentry Monitoring :** Configuration pour ne pas alerter Sentry si le message provient du scheduler esabora [#5978](https://github.com/MTES-MCT/histologe/issues/5978).
- **Configuration CI/CD :** Utilisation de `.env.ci` dans le pipeline CI principal [#5842](https://github.com/MTES-MCT/histologe/issues/5842).
- **Suppression de code :** Suppression du résumé des suivis généré par l'IA [#6025](https://github.com/MTES-MCT/histologe/issues/6025).
- **Gestion des erreurs :** Correction d'une erreur de type sur la normalisation du code INSEE [#6055](https://github.com/MTES-MCT/histologe/issues/6055).

### Autres changements
- **Documentation :** Mise à jour des CGU [#6003](https://github.com/MTES-MCT/histologe/issues/6003).
- **Commandes :** Ajout d'une commande pour mettre à jour les communes fusionnées [#5910](https://github.com/MTES-MCT/histologe/issues/5910).
- **Corrections diverses :** Corrections diverses HTML dans le formulaire bailleur [#6076](https://github.com/MTES-MCT/histologe/issues/6076).
- **Accessibilité :** Amélioration de l'accessibilité du login utilisateur [#6079](https://github.com/MTES-MCT/histologe/issues/6079).
- **Corrections de bugs :** Correction de bugs mineurs et améliorations diverses.
