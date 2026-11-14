## Changelog : rdv-service-public (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois-ci, le service a bénéficié d'améliorations majeures concernant la gestion des visioconférences et la synchronisation des agendas (CalDAV). La sécurité a été renforcée par plusieurs mises à jour critiques du cœur du système, tandis que l'expérience d'administration et le site vitrine ont été enrichis pour offrir une meilleure visibilité sur les fonctionnalités.

### Évolutions fonctionnelles
- **Visioconférences (Visio) :** 
    - Optimisation de l'affichage des liens de réunion : le lien est désormais visible pour l'usager uniquement le jour du rendez-vous [#6878] et le bouton de génération est masqué pour les rendez-vous passés [#6898].
    - Sécurisation des redirections via l'utilisation d'identifiants signés [#6913].
    - Simplification du parcours pour les agents : suppression des bannières de connexion inutiles et élargissement des droits de création de salons visio [#6877, #6861].
- **Synchronisation d'agendas (CalDAV) :** 
    - Amélioration de la lisibilité : affichage des événements "toute la journée" sur une ligne dédiée [#6910] et inclusion de la liste des participants avec leurs emails dans la synchronisation [#6917].
    - Meilleur suivi opérationnel : affichage du statut en cas d'échec de la synchronisation [#6885] et correction du setup pour Zimbra [#6903].
- **Expérience utilisateur & Parcours :** 
    - Mise en place d'un nouveau processus d'invitation à prendre rendez-vous en 3 étapes [#6817].
    - Amélioration de l'accessibilité via une nouvelle gestion de l'autocomplétion des adresses [#6837].
    - Meilleure communication sur la compatibilité des navigateurs avec des messages plus clairs [#6931].
- **Administration & Site Vitrine :** 
    - Enrichissement du site vitrine avec de nouvelles pages (Nouveautés, Fonctionnalités, Webinaire) [#6785, #6848, #6867].
    - Amélioration des outils d'administration pour la gestion des organisations et des agents [#6838, #6836].

### Évolutions techniques
- **Sécurité :** 
    - Mises à jour critiques de Rails [#6924] et Node.js [#6936].
    - Correction de plusieurs vulnérabilités (CVE) impactant le système [#6919, #6905, #6865].
- **Performance & Fiabilité :** 
    - Optimisation du chargement des plages horaires dans le calculateur [#6934].
    - Réduction de la consommation mémoire des applications de revue [#6929].
    - Amélioration de la gestion des tâches de fond : gestion des tentatives (retries) pour Outlook [#6925] et Notion [#6851], et priorisation de l'envoi des codes de connexion par email [#6911].
- **Infrastructure & Core :** 
    - Montée de version majeure vers Ruby 3.4 [#6896] et Rails 8.1 [#6872].
    - Intégration de Sentry pour le suivi des services Menshen (Exchange et Visio) [#6904].
    - Extraction de la configuration Outlook dans une table dédiée pour plus de flexibilité [#6932].

### Autres changements
- Amélioration du confort de développement avec l'ajout du live reload via Hotwire [#6853].
- Nettoyage du code (suppression de code mort) et mises à jour des outils de qualité (Rubocop) [#6842, #6880, #6856].
