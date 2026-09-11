## Changelog : les-emplois (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a considérablement renforcé ses outils de gestion des parcours. Les évolutions majeures concernent la refonte de la gestion des accompagnements (création, modification, archivage) et l'internalisation de la clôture des dossiers PASS IAE, qui ne dépendent plus d'outils tiers. L'expérience utilisateur est également enrichie par un meilleur suivi de la fin des contrats et une identité visuelle affinée.

### Évolutions fonctionnelles
- **Gestion des accompagnements** : Mise en place de nouvelles fonctionnalités pour créer, modifier et archiver les dossiers d'accompagnement. Un nouvel onglet "Conseillers" et des boîtes de revue ont été ajoutés pour améliorer le suivi des candidats.
- **Clôture des PASS IAE** : Les employeurs peuvent désormais clôturer un dossier PASS IAE via un formulaire interne (remplaçant l'usage de Tally), avec une notification automatique envoyée au candidat.
- **Suivi de fin de parcours** : Ajout de bannières d'alerte et de compteurs pour signaler la fin prochaine d'un contrat ou d'un parcours, incluant des suggestions de prochaines étapes pour les candidats.
- **Recherche et filtrage** : Évolution de la recherche "prescripteur" vers une recherche par "accompagnement" et ajout de nouveaux filtres (Handicap, GEIQ, OPCS).
- **Interface et Branding** : Mise à jour de la terminologie et de l'identité visuelle de l'application pour une meilleure cohérence.
- **Alertes** : Ajout de bannières pour annoncer des webinaires thématiques sur le tableau de bord.

### Évolutions techniques
- **Automatisation (Cron)** : Introduction de nouveaux processus automatiques pour l'archivage des anciens accompagnements et la détection de fichiers manquants dans les dossiers.
- **Modèle de données** : Enrichissement du modèle d'accompagnement (nouveaux champs `is_active`, `last_action_at`) et création de nouvelles tables pour le suivi des évaluations GEIQ.
- **API et Sécurité** : Mise à jour des périmètres d'accès (scopes) des API et ajout d'un cookie d'identifiant de navigateur pour améliorer la traçabilité des journaux d'audit.
- **Performance** : Optimisation de la vitesse de migration des CV vers le mode privé.
- **Tests** : Amélioration significative de la couverture de tests, notamment via la création de nouvelles usines de données (factories) pour les professionnels et les accompagnements.

### Autres changements
- **Documentation** : Mise à jour des instructions d'installation locale et correction des liens de la documentation.
- **Qualité du code** : Nettoyage massif de la typographie et des espaces dans les templates pour assurer une présentation visuelle homogène.
