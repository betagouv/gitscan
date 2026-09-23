## Changelog : les-emplois (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois a été marqué par un changement d'identité majeur : le service devient officiellement **La plateforme de l'inclusion**. Parallèlement, l'expérience utilisateur a été enrichie par la création d'un nouvel onglet "Synthèse" pour les bénéficiaires et par une gestion plus fine des accompagnements (création, modification, archivage). Les outils de suivi pour les prescripteurs et employeurs ont également été renforcés, notamment pour anticiper les fins de contrat.

### Évolutions fonctionnelles
- **Identité visuelle** : Rebranding complet du projet vers "La plateforme de l'inclusion" (nouveau nom, logos, textes légaux et documentation).
- **Gestion des bénéficiaires** : 
    - Création d'un onglet "Synthèse" (Overview) regroupant les informations clés : conseillers référents, détails du contrat et dernières candidatures.
    - Amélioration de la visibilité des alertes concernant les fins de contrat pour les prescripteurs et les employeurs.
- **Accompagnements** : 
    - Mise en place de nouvelles actions pour les accompagnements : création, édition et archivage.
    - Ajout de filtres de recherche pour mieux gérer les listes d'accompagnements.
- **Processus d'approbation (PASS IAE)** : 
    - Possibilité pour les employeurs de clôturer un PASS IAE directement via un formulaire interne.
    - Notification automatique des bénéficiaires lors de la clôture de leur dossier.
- **Orientation et Insertion** : 
    - Amélioration du processus d'orientation avec la gestion des pièces jointes et une nouvelle API de récupération par structure.
    - Possibilité de forcer la synchronisation des données d'insertion.
- **Interface et Accessibilité** : 
    - Ajout d'une déclaration d'accessibilité détaillant les non-conformités.
    - Amélioration de l'ergonomie des formulaires de recherche (villes) et de l'affichage des messages d'erreur.

### Évolutions techniques
- **Traçabilité et Audit** : Implémentation d'une piste d'audit (audit trail) de base incluant l'utilisation de `X-Forwarded-For` et l'ajout d'un identifiant de navigateur pour le suivi.
- **Sécurité et Confidentialité** : 
    - Sécurisation des mises à jour des données des salariés.
    - Renforcement de la protection des données : l'identité des bénéficiaires est désormais exclue des rapports Sentry.
    - Généralisation de l'usage de ProConnect pour les professionnels et les institutionnels.
- **Qualité de code et Performance** : 
    - Correction massive des erreurs de typage (mypy) et mise en conformité avec les règles de formatage (djlint).
    - Optimisation de certaines tâches planifiées (cron) pour améliorer la rapidité des migrations de données.
    - Refactoring de la logique métier (extraction de fonctions communes pour l'administration et les approbations).
- **Infrastructure et CI/CD** : 
    - Modification du workflow de CI (arrêt du build automatique sur la branche main).
    - Optimisation de la verbosité des tests pour faciliter le débogage.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique (explications SSO, procédures d'installation locale).
- **Nettoyage** : Suppression de composants obsolètes (application GPS, application de recommandations) et nettoyage général du formatage du code (espaces, typographies).
