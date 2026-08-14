## Changelog : rdv-service-public (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par une modernisation importante de l'infrastructure (passage à Rails 8 et Ruby 3.4) et une amélioration notable de l'expérience utilisateur grâce à l'intégration plus poussée du Design System de l'État (DSFR). Les fonctionnalités de visioconférence ont été introduites, et de nombreux correctifs ont été apportés pour fluidifier la prise de rendez-vous et la gestion des agents.

### Évolutions fonctionnelles
- **Expérience usager** :
    - Simplification du parcours de prise de rendez-vous avec la fusion des étapes après connexion [#6421].
    - Amélioration de la vue de sélection des créneaux et clarification des consignes sur les motifs de rendez-vous [#6591, #6598].
    - Correction des liens de reprise de rendez-vous après une annulation (email et SMS) [#6535].
- **Interface et gestion des agents** :
    - Intégration de FullCalendar v7 et mise à jour de l'interface de planification [#6506, #6589].
    - Enrichissement du tableau de bord agent : affichage des invitations en attente [#6588] et menu déroulant plus complet [#6549].
    - Amélioration visuelle via le DSFR (modales, menu latéral, couleurs des motifs) [#6578, #6512, #6582].
- **Visioconférence** :
    - Ajout de la fonctionnalité de visioconférence et possibilité de la désactiver par instance [#6536, #6565].
- **Corrections et fiabilité** :
    - Résolution de problèmes sur la gestion des horaires, les rendez-vous collectifs et la prise de rendez-vous pour un tiers [#6599, #6556, #6594].
    - Amélioration de la recherche d'usagers (numéros de téléphone, redirections, recherche géographique) [#6546, #6560, #6456].
    - Correction de la synchronisation des fuseaux horaires avec Outlook [#6527].

### Évolutions techniques
- **Mises à jour majeures** :
    - Migration vers Ruby 3.4.10 [#6505] et Rails 8.0.5.1 [#6572].
    - Passage de Sprockets à Propshaft pour la gestion des assets [#6576].
- **Performance et Observabilité** :
    - Optimisation de la mémoire lors de l'exécution des exports [#6597].
    - Renforcement du logging (paramètres d'API, recherches usagers) et du suivi des erreurs (Sentry, Zammad) [#6596, #6564, #6586, #6562].
    - Refactorisation de composants clés comme le mailer d'export et la gestion des notifications de rendez-vous [#6600, #6590].
- **Infrastructure et Tests** :
    - Amélioration de la stabilité des tests en réduisant la "flakiness" [#6533, #6534].
    - Amélioration de la gestion des webhooks et de l'intégration Brevo pour les emails [#6575, #6542].

### Autres changements
- **Accessibilité** : Amélioration de la structure HTML (listes) pour les nouveaux rendez-vous collectifs [#6508].
- **Documentation** : Ajout de documentation et de scripts pour le déploiement d'environnements dédiés aux agents LLM [#6492].
