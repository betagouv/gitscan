## Changelog : monlogementetudiant (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec le lancement de l'espace étudiant, permettant désormais de sauvegarder des simulations de budget et de les télécharger en PDF. Les outils de gestion pour les administrateurs et gestionnaires ont été considérablement enrichis avec de nouvelles capacités d'exportation de données, un meilleur suivi des statistiques et une gestion des permissions plus fine et sécurisée.

### Évolutions fonctionnelles
- **Espace Étudiant** : 
    - Création d'un espace de travail permettant de sauvegarder les calculs de budget et de les exporter au format PDF.
    - Gestion des favoris et des préférences de notifications.
- **Gestion & Administration** :
    - **Permissions** : Simplification et affinement des droits des gestionnaires (gestion des contacts par résidence spécifique et conditionnement de la gestion des candidats au parcours).
    - **Exports de données** : Ajout de nouveaux exports CSV incluant les statistiques des résidences, les informations de contact des gestionnaires et les URLs de présentation des propriétaires.
    - **Pilotage** : Amélioration du tableau de bord avec le suivi des connexions des gestionnaires, la visibilité sur la part d'étudiants boursiers et de nouveaux outils de pré-audit.
- **Recherche & Interface** :
    - **Recherche** : Correction des limites de recherche par département et des redirections de slugs de villes.
    - **Expérience utilisateur** : Amélioration de l'accessibilité (a11y), alignement des résultats de recherche et mise à jour des composants d'interface vers les standards DSFR (champs de saisie, menus latéraux, alertes).
- **Alertes** : Optimisation de l'ordre de déclenchement des alertes (expiration avant détection de nouvelles disponibilités) et ajout d'une commande pour désactiver des campagnes d'alerte.

### Évolutions techniques
- **Données & Archivage** : 
    - Mise en place d'une politique de rétention automatique (7 mois pour les événements de suivi) avec purge mensuelle et archivage sécurisé sur S3.
    - Automatisation des sauvegardes quotidiennes et mensuelles de la base de données sur S3.
- **Performance & Infrastructure** :
    - Mise en cache des images pour accélérer le chargement.
    - Optimisation des tâches de fond (cron) pour respecter les limites de ressources (fusion des jobs de détection d'alertes).
    - Optimisation des connexions à la base de données.
- **Analytics** : Amélioration du suivi des visites provenant de widgets partenaires via Matomo et optimisation du marquage des appels à l'action (CTA).
- **Maintenance du code** : Refactorisation de la gestion des dates avec `dayjs` et correction de problèmes de rendu côté serveur (SSR) avec `dompurify`.

### Autres changements
- Mise à jour de la politique de confidentialité.
- Amélioration de la documentation technique concernant les procédures de restauration et la visibilité des archives S3.
- Nettoyage général du code (formatage Biome, suppression de code mort et de commentaires inutiles).
