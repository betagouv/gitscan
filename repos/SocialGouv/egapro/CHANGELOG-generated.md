## Changelog : egapro (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des problèmes d'interface et en affinant les étapes de la déclaration. Des efforts importants ont également été consacrés à l'amélioration de l'infrastructure et de l'automatisation des processus de déploiement, ainsi qu'à l'ajout de nouvelles fonctionnalités pour l'administration et le suivi des données.

### Évolutions fonctionnelles
- Amélioration de l'interface de connexion : l'image est maintenant alignée en haut et le fond bleu est limité au conteneur principal. [#3464](https://github.com/SocialGouv/egapro/issues/3464)
- Correction du déconnexion OIDC : la déconnexion initiée par le fournisseur d'identité (RP-initiated logout) fonctionne correctement côté navigateur. [#3347](https://github.com/SocialGouv/egapro/issues/3347)
- Gestion du statut "annulé" pour les déclarations. [#3431](https://github.com/SocialGouv/egapro/issues/3133)
- Ajout de colonnes de pourcentages dans la déclaration. [#3405](https://github.com/SocialGouv/egapro/issues/3379)
- Pré-remplissage des données de la déclaration à partir de la dernière soumission, notamment pour l'indicateur 7. [#3269](https://github.com/SocialGouv/egapro/issues/3246)
- Amélioration de la page de récapitulatif de la rémunération (lecture seule). [#3375](https://github.com/SocialGouv/egapro/issues/3375)
- Correction de l'alignement et de l'accessibilité de l'étape "Effectifs" et du modal CSE. [#3371](https://github.com/SocialGouv/egapro/issues/3320) et [#3370](https://github.com/SocialGouv/egapro/issues/3325)
- Correction du lien "Précédent" dans le récapitulatif pour retourner à l'étape 5 après soumission. [#3384](https://github.com/SocialGouv/egapro/issues/3266)
- Correction d'un bug empêchant l'affichage correct d'un message d'erreur lorsque la source est manquante pour un indicateur. [#3383](https://github.com/SocialGouv/egapro/issues/3383)
- Amélioration de l'interface utilisateur de "Mon Espace" et de la page de connexion, en suivant les retours Figma. [#3344](https://github.com/SocialGouv/egapro/issues/3319) et [#3340](https://github.com/SocialGouv/egapro/issues/3318)
- Ajout d'une page de recherche publique pour les référents. [#3234](https://github.com/SocialGouv/egapro/issues/3186)
- Ajout d'un sitemap et d'un fichier robots.txt pour le SEO. [#3235](https://github.com/SocialGouv/egapro/issues/3235)

### Évolutions techniques
- Documentation de l'architecture et des fonctionnalités de EGAPRO V2. [#3390](https://github.com/SocialGouv/egapro/issues/3390) et [#3389](https://github.com/SocialGouv/egapro/issues/3389)
- Refactorisation de la gestion des filtres pour les référents dans l'administration et la recherche publique. [#3282](https://github.com/SocialGouv/egapro/issues/3281) et [#3276](https://github.com/SocialGouv/egapro/issues/3276)
- Mise en place d'une couche de cache Redis avec Valkey pour améliorer les performances de Next.js. [#3228](https://github.com/SocialGouv/egapro/issues/3228)
- Intégration de Tipimail pour l'envoi des accusés de réception par email. [#3238](https://github.com/SocialGouv/egapro/issues/3177)
- Amélioration du pipeline CI/CD : consolidation de la configuration, discipline de logging, détection des blocages, rapports automatiques. [#3423](https://github.com/SocialGouv/egapro/issues/3423)
- Ajout d'un agent "doc-writer" pour la documentation et intégration avec une boucle épique. [#3409](https://github.com/SocialGouv/egapro/issues/3409)
- Ajout d'un composant API Gateway. [#3304](https://github.com/SocialGouv/egapro/issues/3304)
- Amélioration de l'observabilité du pipeline avec des événements de phase, un suivi des coûts en temps réel et une détection des blocages. [#3410](https://github.com/SocialGouv/egapro/issues/3410)
- Ajout d'un script de post-processing et d'un workflow pour les annotations SUIT/GIP-MDS. [#3341](https://github.com/SocialGouv/egapro/issues/3341)

### Autres changements
- Miroitement de la documentation vers le wiki GitHub sur les branches alpha/master. [#3408](https://github.com/SocialGouv/egapro/issues/3408)
- Correction de l'alignement et de l'accessibilité de plusieurs éléments de l'interface utilisateur, en suivant les retours Figma. [#3361](https://github.com/SocialGouv/egapro/issues/3324), [#3330](https://github.com/SocialGouv/egapro/issues/3321) et [#3339](https://github.com/SocialGouv/egapro/issues/3317)
- Suppression des filtres Index et Valeur dans l'administration. [#3279](https://github.com/SocialGouv/egapro/issues/3279)
- Ajout d'un lien "Déclarations" dans le menu latéral de l'administration. [#3275](https://github.com/SocialGouv/egapro/issues/3275)
- Suppression de la nécessité de spécifier un sous-domaine pour les builds de préproduction.
- Correction de plusieurs problèmes mineurs d'interface utilisateur et d'accessibilité.
