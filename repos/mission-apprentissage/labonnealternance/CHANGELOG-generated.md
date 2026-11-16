## Changelog : labonnealternance (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci, la plateforme a considérablement renforcé ses capacités de gestion de contenu grâce au déploiement de nouveaux outils de modération et à la publication du baromètre T2-T3 2026. L'expérience de recherche a été affinée, notamment via une meilleure intégration avec Mon Master, tandis que la robustesse et la sécurité du système ont été consolidées par des mises à jour critiques et une optimisation des processus de déploiement.

### Évolutions fonctionnelles
- **Modération & Administration** : Déploiement du nouveau back-office pour la modération des offres libres ([#5499](https://github.com/mission-apprentissage/labonnealternance/issues/5499)) et amélioration de l'interface de modération (notes des agents, pastilles de conformité et navigation entre les offres) ([#5868](https://github.com/mission-apprentissage/labonnealternance/issues/5868)).
- **Recherche & Découverte** : Amélioration de l'intégration avec Mon Master (recherche par code RNCP et par commune) et optimisation de l'affichage des résultats (gestion des états vides, priorité aux candidatures simplifiées et correction du calcul de l'ancienneté des offres).
- **Expérience Utilisateur (UX/UI)** : Mise à jour des visuels (carte étudiant, guide de l'alternant), amélioration de l'accessibilité (modales, navigation au clavier sur les tableaux) et ajout de nouveaux éléments d'interface (bandeau conseiller, mise en avant des "smart apply").
- **Données & SEO** : Publication du baromètre T2-T3 2026, optimisation du référencement naturel (titres et méta-descriptions par secteur) et amélioration de la précision des données (gestion des comptes par SIRET et des codes IDCC).

### Évolutions techniques
- **Sécurité & Infrastructure** : Application de correctifs de sécurité critiques (Node.js, Next.js), rotation des secrets SOPS et renforcement de la protection contre le spam via la configuration du rate limiting sur Nginx.
- **Pipeline CI/CD & Tests** : Optimisation de la durée des jobs de CI, amélioration de l'intégration des scans de sécurité Docker Scout et stabilisation des tests de base de données (MongoDB) en environnement de test.
- **Backend & Data Ingestion** : Mise en place d'un nouveau socle de détection d'alertes (règles planifiées et déduplication) et optimisation du traitement des flux partenaires (rafraîchissement ciblé uniquement sur les données modifiées).
- **Observabilité** : Amélioration de la journalisation (utilisation de Pino) et enrichissement des logs d'accès pour un meilleur suivi des requêtes serveur.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique (`AGENTS.md`).
- **Maintenance** : Nettoyage du code (suppression de code mort).
