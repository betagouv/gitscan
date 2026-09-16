## Changelog : les-emplois (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois a été marqué par un changement d'identité majeur avec le passage du nom du service à "La plateforme de l'inclusion". Les évolutions se sont concentrées sur l'amélioration de la gestion des accompagnements (création, modification et archivage des affectations), le renforcement de la sécurité et de la traçabilité des données, ainsi que l'ajout d'outils de pilotage pour les employeurs afin d'anticiper les fins de contrat.

### Évolutions fonctionnelles
- **Identité visuelle et terminologie** : Changement de nom pour "La plateforme de l'inclusion", mise à jour des logos, des images de partage et de la terminologie (notamment autour des PASS IAE).
- **Gestion des accompagnements** : 
    - Nouvelles capacités pour créer, modifier et archiver les affectations des demandeurs d'emploi.
    - Amélioration de l'interface des conseillers avec de nouveaux filtres et une meilleure organisation des vues.
    - Possibilité pour les prescripteurs de demander un bilan d'accompagnement à une structure (SIAE).
- **Pilotage employeur et structures** :
    - Ajout de compteurs et de bannières pour identifier les salariés en fin de contrat et suggérer des parcours de suite.
    - Possibilité pour les employeurs de clôturer un PASS IAE directement via un formulaire interne.
    - Réorganisation des menus de navigation pour les prescripteurs, les employeurs et les structures.
- **Recherche et navigation** :
    - Amélioration des moteurs de recherche et ajout de nouveaux filtres (notamment sur le handicap et les acteurs IAE).
    - Optimisation de l'expérience utilisateur (UX) : utilisation de notifications temporaires (toasts) au lieu de pages de confirmation, et meilleur tri des candidatures.

### Évolutions techniques
- **Sécurité et confidentialité** : 
    - Mise en place d'une piste d'audit (audit trail) pour tracer les actions.
    - Renforcement de la protection de la vie privée en s'assurant que l'identité des demandeurs d'emploi n'est pas transmise aux outils de suivi d'erreurs (Sentry).
- **Authentification** : Généralisation de l'utilisation de ProConnect pour l'ensemble des profils professionnels (institutionnels, prescripteurs, employeurs).
- **Données et Analytics** : 
    - Enrichissement des tableaux de bord Metabase (données GEIQ, analyse des délais de transition par état).
    - Amélioration du suivi statistique via Matomo.
- **Optimisation et maintenance** : 
    - Optimisation des performances des tâches automatisées (cron jobs).
    - Refactorisation de plusieurs composants pour supprimer des requêtes redondantes et améliorer la rapidité de l'application.

### Autres changements
- **Documentation** : Amélioration des guides d'installation locale et ajout de documentation sur le fonctionnement du SSO.
- **Nettoyage** : Suppression de modules obsolètes (GPS, recommandations) et corrections massives de formatage (espacements, typographie) pour harmoniser le code et l'interface.
