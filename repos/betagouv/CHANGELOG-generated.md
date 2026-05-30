# Synthèse d'activité : betagouv (du 10/05 au 07/06)

## Résumé de l'activité
L'activité récente de l'organisation betagouv s'est concentrée sur l'amélioration de la robustesse et de la sécurité de ses outils, avec de nombreuses mises à jour de dépendances et corrections de vulnérabilités.  Plusieurs projets ont bénéficié d'améliorations significatives de l'expérience utilisateur, notamment `jeveuxaider-front`, `mon-service-securise`, `infomedicament`, et `sylvasan`.  De nouveaux services ont été ajoutés ou améliorés, comme l'intégration de Matomo dans `turgot-metabase` et l'ajout de fonctionnalités de gestion des utilisateurs dans `mission-transition-ecologique`.  Plusieurs projets ont également progressé dans la modernisation de leur infrastructure et de leur code, comme `mle-front` et `infomedicament-dataeng`.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- Correction d'une vulnérabilité XSS potentielle dans [seves](/repos/betagouv/seves).
- Mise à jour de la gem `rack-session` dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) pour corriger une vulnérabilité critique.
- Correction de failles de sécurité dans [mon-entreprise](/repos/betagouv/mon-entreprise).
- Mise à jour de dépendances critiques dans [grist-cron-grist-to-brevo](/repos/betagouv/grist-cron-grist-to-brevo).

## Autres changements notables
- Refonte complète de l'architecture de [pitchou](/repos/betagouv/pitchou) vers SvelteKit pour améliorer les performances.
- Migration vers Symfony 8.0 et Doctrine 8.0 dans [mon-aide-cyber-journal](/repos/betagouv/mon-aide-cyber-journal).
- Passage à Poetry pour la gestion des dépendances dans [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng).
- Amélioration de la gestion des droits d'accès dans [grist-budget-agriculture](/repos/betagouv/grist-budget-agriculture).
- Ajout d'une synchronisation entre Turgot et Matomo dans [kube-dev](/repos/betagouv/kube-dev).

## Dépôts les plus actifs
- [seves](/repos/betagouv/seves) : Amélioration de l'interface utilisateur, corrections de sécurité et gestion des documents.
- [pitchou](/repos/betagouv/pitchou) : Refonte complète de l'architecture et amélioration de la sécurité.
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Amélioration de la gestion des administrateurs et refonte du parcours d'homologation.
- [infomedicament](/repos/betagouv/infomedicament) : Amélioration des performances et de l'expérience utilisateur.
- [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Amélioration de l'interface et ajout de nouvelles fonctionnalités.
- [grist-core](/repos/betagouv/grist-core) : Amélioration de l'importation depuis Airtable et de la comparaison de documents.
- [sylvasan](/repos/betagouv/sylvasan) : Ajout d'authentification OAuth2 et de nouvelles fonctionnalités pour la gestion des enquêtes.
